import uuid
from datetime import datetime
from hashlib import blake2b
from secrets import randbits
from time import time
from typing import Optional, FrozenSet

from kaiju_db.services import DatabaseService, SQLService
from kaiju_tools.cache import BaseCacheService
from kaiju_tools.services import Scope, Session
from kaiju_tools.serialization import Serializable
from kaiju_tools.exceptions import NotFound

from kaiju_auth.tables import sessions_table

__all__ = ['SessionService', 'UserSession', 'USER_SCOPE', 'SYSTEM_SCOPE']


USER_SCOPE = 'user'
SYSTEM_SCOPE = 'system'


class UserSession(Serializable, Session):
    """User session data."""

    __slots__ = ('id', 'h_agent', 'user_id', 'expires', 'permissions', 'data', 'created', '_stored', '_changed')

    def __init__(
        self,
        *,
        id: str,
        h_agent: bytes,
        user_id: Optional[uuid.UUID],
        expires: int,
        permissions: FrozenSet[str],
        data: dict,
        created: datetime,
        _stored: bool,
        _changed: bool,
        _loaded: bool,
    ):
        """Initialize.

        :param id:
        :param h_agent:
        :param user_id:
        :param expires:
        :param permissions:
        :param data:
        :param created:
        :param _stored:
        :param _changed:
        :param _loaded:
        """
        self.id = id
        self.h_agent = h_agent
        self.user_id = user_id
        self.expires = expires
        self.permissions = frozenset(permissions)
        self.data = data
        self.created = created
        self._stored = _stored
        self._changed = _changed
        self._loaded = _loaded
        if SYSTEM_SCOPE in self.permissions:
            self._scope = Scope.SYSTEM
        elif USER_SCOPE in self.permissions:
            self._scope = Scope.USER
        else:
            self._scope = Scope.GUEST

    def __getitem__(self, item):
        return self.data.get(item)

    def __setitem__(self, key, value):
        self.update({key: value})

    @property
    def scope(self) -> Scope:
        """Base user scope."""
        return self._scope

    @property
    def stored(self) -> bool:
        """Session should be stored."""
        return self._stored

    @property
    def changed(self) -> bool:
        """Session has changed."""
        return self._changed

    @property
    def loaded(self) -> bool:
        """Session has been loaded from db."""
        return self._loaded

    def update(self, data: dict):
        """Update session data."""
        self.data.update(data)
        self._changed = True

    def clear(self):
        """Clear all session data."""
        self.data.clear()
        self._changed = True

    def repr(self) -> dict:
        """Get object representation."""
        return {slot: getattr(self, slot) for slot in self.__slots__ if not slot.startswith('_')}


class SessionService(SQLService):
    """Session store base class."""

    service_name = 'sessions'
    table = sessions_table
    session_key = 'session:{session_id}'

    def __init__(
        self,
        app,
        database_service: DatabaseService = None,
        cache_service: BaseCacheService = None,
        session_idle_timeout: int = 24 * 3600,
        exp_renew_interval: int = 3600,
        salt: str = 'SHT',
        logger=None,
    ):
        """Initialize.

        :param app:
        :param database_service:
        :param cache_service:
        :param session_idle_timeout: (s) Idle life timeout each session.
        :param exp_renew_interval: (s)
        :param salt: set your salt
        :param logger:
        """
        super().__init__(app, database_service, logger=logger)
        self._cache: BaseCacheService = self.discover_service(cache_service, cls=BaseCacheService)
        self.session_idle_timeout = session_idle_timeout
        self.exp_renew_interval = exp_renew_interval
        self.salt = salt.encode('utf-8')

    def get_new_session(self, data: dict, *, user_agent: str = '') -> UserSession:
        """Create and return a new session (not stored yet).

        :param data:
        :param user_agent: user agent or client id for security purposes
        """
        h_agent = self._get_agent_hash(user_agent)
        session = self._create_new_session(data, h_agent)
        self.logger.info('New session: %s', session.id)
        return session

    async def save_session(self, session: UserSession, /) -> None:
        """Save session to the storage.

        The session will be stored only if it is marked as stored, and it has been changed.
        Token-auth sessions and initial sessions without data won't be stored.
        """
        if not session or not session.stored:
            return

        key = self._get_session_key(session.id)
        exp = int(time()) + self.session_idle_timeout

        if session.changed:
            self.logger.info('Saving session: %s', session.id)
            data = session.repr()
            data['expires'] = exp
            on_conflict_values = data.copy()
            del on_conflict_values['id']
            del on_conflict_values['h_agent']
            del on_conflict_values['created']
            key = self._get_session_key(session.id)
            await self._cache.set(key, session.repr(), ttl=exp, nowait=True)
            await self.create(
                data,
                columns=[],
                on_conflict='do_update',
                on_conflict_keys=['id'],
                on_conflict_values=on_conflict_values,
            )
        elif session.loaded and session.expires - time() < self.exp_renew_interval:
            asyncio.create_task(self._cache._transport.expire(key, exp))  # noqa
            await self.update(session.id, {'expires': exp}, columns=[])

    async def delete_session(self, session: UserSession, /) -> None:
        """Delete session from the storage."""
        if session and session.stored and session.loaded:
            self.logger.info('Removing session: %s', session.id)
            key = self._get_session_key(session.id)
            await self._cache.delete(key, nowait=True)
            await self.delete(session.id, columns=[])

    async def load_session(self, session_id: str, /, *, user_agent: str = '') -> Optional[UserSession]:
        """Load session from the storage.

        :param session_id: unique session id
        :param user_agent: user agent or client id for security purposes
        :return: returns None when session is not available
        """
        key = self._get_session_key(session_id)
        session = cached = await self._cache.get(key)
        if not session:
            try:
                session = await self.get(session_id)
            except NotFound:
                self.logger.info('Session not found: %s', session_id)
                return

            if session['expires'] < time():
                self.logger.debug('Session expired: %s', session_id)
                await self._cache.delete(key, nowait=True)
                await self.delete(session_id)
                return

        agent_hash = self._get_agent_hash(user_agent)
        session = UserSession(**session, _stored=True, _changed=False, _loaded=True)
        if session.h_agent != agent_hash:
            self.logger.info('User agent mismatch: %s', session_id)
            return

        self.logger.debug('Loaded session: %s', session_id)
        if not cached:
            await self._cache.set(key, session.repr(), nowait=True)
        return session

    def _create_new_session(self, data: dict, h_agent: bytes) -> UserSession:
        """Create a new session object."""
        return UserSession(
            id=uuid.UUID(int=randbits(128)).hex,
            user_id=None,
            permissions=frozenset(),
            data=data,
            expires=int(time()) + self.session_idle_timeout,
            created=datetime.now(),
            h_agent=h_agent,
            _changed=bool(data),
            _stored=True,
            _loaded=False,
        )

    def _get_session_key(self, session_id: str, /) -> str:
        return self.session_key.format(session_id=session_id)

    def _get_agent_hash(self, user_agent: str, /) -> bytes:
        return blake2b(user_agent.encode('utf-8'), digest_size=16, salt=self.salt).digest()
