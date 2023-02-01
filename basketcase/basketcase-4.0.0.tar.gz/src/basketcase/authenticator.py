import typing

if typing.TYPE_CHECKING:
    import requests
    from . import storage


class Authenticator:
    def __init__(
        self,
        http_client: 'requests.Session',
        storage_manager: 'storage.Storage'
    ):
        self._http_client = http_client
        self._storage = storage_manager

    def new_session(
            self,
            cookie_id: str,
            description: str,
            is_default: bool
    ) -> int:
        session_id = self._storage.insert(description, cookie_id, is_default)
        return session_id
    
    def list_sessions(self):
        sessions = self._storage.get_all()

        for session in sessions:
            description = session['first_used']

            if session['description']:
                description = session['description']
            
            if session['is_default']:
                description += ' (default)'

            print(f'{session["rowid"]!s}: {description}')

    def delete_session(self, id: int):
        session = self._storage.get_one_by_id(id)

        if not session:
            raise RuntimeError(f'Session not found')
        
        self._storage.delete(session)

    def load_session(self, id: int):
        session = self._storage.get_one_by_id(id)

        if session:
            self._http_client.cookies.set('sessionid', session['cookie_id'])

    def load_default_session(self):
        sessions = self._storage.get_all()

        if len(sessions) == 1:
            # A single session is treated as the default
            self._http_client.cookies.set('sessionid', sessions[0]['cookie_id'])
        else:
            for session in sessions:
                if not session['is_default']:
                    continue

                self._http_client.cookies.set('sessionid', session['cookie_id'])

    def set_default_session(self, id: int):
        session = self._storage.get_one_by_id(id)

        if not session:
            raise RuntimeError(f'Session not found')

        if session['is_default']:
            raise RuntimeError('Session is already default')

        self._storage.reset_default()

        session_dict = {
            'rowid': session['rowid'],
            'description': session['description'],
            'cookie_id': session['cookie_id'],
            'is_default': session['is_default'],
        }

        session_dict['is_default'] = 1
        self._storage.update(session_dict)
    
    def unset_default_session(self):
        self._storage.reset_default()