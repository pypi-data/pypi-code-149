# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/client/95_DomoAuth.ipynb.

# %% auto 0
__all__ = ['get_full_auth', 'get_developer_auth', 'test_access_token', 'DomoAuth', 'InvalidCredentialsError',
           'InvalidInstanceError', 'DomoFullAuth', 'DomoTokenAuth', 'DomoDeveloperAuth']

# %% ../../nbs/client/95_DomoAuth.ipynb 3
from dataclasses import dataclass, field
from abc import abstractmethod
from typing import Optional, Union

import aiohttp

import domolibrary.client.ResponseGetData as rgd

# %% ../../nbs/client/95_DomoAuth.ipynb 5
async def get_full_auth(
    domo_instance: str,  # domo_instance.domo.com
    domo_username: str,  # email address
    domo_password: str,
    session: Optional[aiohttp.ClientSession] = None,
    debug_api: bool = False
) -> rgd.ResponseGetData:
    """uses username and password authentication to retrieve a full_auth access token"""

    is_close_session = False

    if not session:
        is_close_session = True
        session = aiohttp.ClientSession()

    url = f"https://{domo_instance}.domo.com/api/content/v2/authentication"

    tokenHeaders = {"Content-Type": "application/json"}

    body = {
        "method": "password",
        "emailAddress": domo_username,
        "password": domo_password,
    }

    if debug_api:
        print(body, url)

    res = await session.request(method="POST", url=url, headers=tokenHeaders, json=body)

    if is_close_session:
        await session.close()

    return await rgd.ResponseGetData._from_aiohttp_response(res)

# %% ../../nbs/client/95_DomoAuth.ipynb 12
async def get_developer_auth(
    domo_client_id: str,
    domo_client_secret: str,
    session: Optional[aiohttp.ClientSession] = None,
    debug_api: bool = False
) -> rgd.ResponseGetData:

    """
    only use for authenticating against apis documented under developer.domo.com
    """
    is_close_session = False

    if not session:
        is_close_session = True
        session = aiohttp.ClientSession(
            auth=aiohttp.BasicAuth(domo_client_id, domo_client_secret)
        )

    url = f"https://api.domo.com/oauth/token?grant_type=client_credentials"

    if debug_api:
        print(url, domo_client_id, domo_client_secret)

    res = await session.request(method="GET", url=url)

    if is_close_session:
        await session.close()

    return await rgd.ResponseGetData._from_aiohttp_response(res)

# %% ../../nbs/client/95_DomoAuth.ipynb 16
async def test_access_token(
    domo_access_token: str,  # as provided in Domo > Admin > Authentication > AccessTokens
    domo_instance: str,  # <domo_instance>.domo.com
    session: Optional[aiohttp.ClientSession] = None,
    debug_api: bool = False
):
    """
    will attempt to validate against the 'me' API.
    This is the same authentication test the Domo Java CLI uses.
    """

    is_close_session = False

    if not session:
        is_close_session = True
        session = aiohttp.ClientSession()

    url = f"https://{domo_instance}.domo.com/api/content/v2/users/me"

    tokenHeaders = {"X-DOMO-Developer-Token": domo_access_token}

    if debug_api:
        print(url,tokenHeaders)

    res = await session.request(method="GET", headers=tokenHeaders, url=url)

    if is_close_session:
        await session.close()

    return await rgd.ResponseGetData._from_aiohttp_response(res)

# %% ../../nbs/client/95_DomoAuth.ipynb 20
@dataclass
class _DomoAuth_Required:
    """required parameters for all Domo Auth classes"""

    domo_instance: str

    def __post_init__(self):
        if self.domo_instance:
            self.set_manual_login()

    def set_manual_login(self):
        self.url_manual_login = (
            f"https://{self.domo_instance}.domo.com/auth/index?domoManualLogin=true"
        )


@dataclass
class _DomoAuth_Optional:
    """parameters are defined after initialization"""

    token: Optional[str] = field(default=None, repr=False)
    token_name: Optional[str] = field(default=None)
    user_id: Optional[str] = field(default=None, repr=False)
    auth_header: dict = field(default_factory=dict, repr=False)

    url_manual_login: Optional[str] = None

    async def get_auth_token(self) -> Union[str, None]:
        """placeholder method"""
        pass

    async def generate_auth_header(self) -> Union[dict, None]:
        """returns auth header appropriate for this authentication method"""
        pass

    async def print_is_token(self, token_name=None) -> None:
        self.token_name = token_name or self.token_name

        if not self.token:
            await self.get_auth_token()

        token_str = f"{self.token_name} "

        if not self.token:
            print(
                f"🚧 failed to retrieve {token_str if token_name else ''}token from {self.domo_instance}")
            return False

        print(
            f"🎉 {token_str if token_name else ''}token retrieved from {self.domo_instance} ⚙️")
        return True


# %% ../../nbs/client/95_DomoAuth.ipynb 21
@dataclass
class DomoAuth(_DomoAuth_Optional, _DomoAuth_Required):
    """abstract DomoAuth class"""

# %% ../../nbs/client/95_DomoAuth.ipynb 25
class DomoErrror(Exception):
    """base exception"""

    def __init__(
        self,
        status: Optional[int] = None,  # API request status
        message: str = "error",  # <domo_instance>.domo.com
        domo_instance: Optional[str] = None,
    ):

        instance_str = f" at {domo_instance}" if domo_instance else ""
        status_str = f"Status {status} - " if status else ""
        self.message = f"{status_str}{message}{instance_str}"
        super().__init__(self.message)

# %% ../../nbs/client/95_DomoAuth.ipynb 26
class InvalidCredentialsError(DomoErrror):
    """return invalid credentials sent to API"""

    def __init__(
        self,
        status: Optional[int] = None,  # API request status
        message="invalid credentials",
        domo_instance: Optional[str] = None,
    ):

        super().__init__(status=status, message=message, domo_instance=domo_instance)


class InvalidInstanceError(DomoErrror):
    """return if invalid domo_instance sent to API"""

    def __init__(
        self,
        status: Optional[int] = None,
        message="invalid instance",
        domo_instance: Optional[str] = None,
    ):
        super().__init__(status=status, message=message, domo_instance=domo_instance)

# %% ../../nbs/client/95_DomoAuth.ipynb 29
@dataclass
class _DomoFullAuth_Required(_DomoAuth_Required):
    """mix requied parameters for DomoFullAuth"""

    domo_username: str
    domo_password: str = field(repr=False)


# %% ../../nbs/client/95_DomoAuth.ipynb 30
@dataclass
class DomoFullAuth(_DomoAuth_Optional, _DomoFullAuth_Required):
    """use for full authentication token"""

    def generate_auth_header(self, token: str) -> dict:
        self.auth_header = {"x-domo-authentication": token}
        return self.auth_header

    async def get_auth_token(
        self,
        session: Optional[aiohttp.ClientSession] = None,
        debug_api : bool = False
    ) -> str:
        """returns `token` if valid credentials provided else raises Exception and returns None"""

        res = await get_full_auth(
            domo_instance=self.domo_instance,
            domo_username=self.domo_username,
            domo_password=self.domo_password,
            session=session,
            debug_api = debug_api
        )

        if res.is_success and res.response.get("reason") == "INVALID_CREDENTIALS":
            raise InvalidCredentialsError(
                status=res.status,
                message=str(res.response.get("reason")),
                domo_instance=self.domo_instance,
            )

        if res.status == 403:
            raise InvalidInstanceError(
                status=res.status,
                message="INVALID INSTANCE",
                domo_instance=self.domo_instance,
            )

        token = str(res.response.get("sessionToken"))
        self.token = token
        self.user_id = str(res.response.get("userId"))

        self.auth_header = self.generate_auth_header(token=token)

        if not self.token_name:
            self.token_name = "full_auth"

        return self.token

# %% ../../nbs/client/95_DomoAuth.ipynb 36
@dataclass
class _DomoTokenAuth_Required(_DomoAuth_Required):
    """mix requied parameters for DomoFullAuth"""

    domo_access_token: str = field(repr=False)

# %% ../../nbs/client/95_DomoAuth.ipynb 37
@dataclass
class DomoTokenAuth(_DomoAuth_Optional, _DomoTokenAuth_Required):
    """
    use for access_token authentication.
    Tokens are generated in domo > admin > access token
    Necessary in cases where direct sign on is not permitted
    """

    def generate_auth_header(self, token: str) -> dict:
        self.auth_header = {"x-domo-developer-token": token}
        return self.auth_header

    async def get_auth_token(
        self, session: Optional[aiohttp.ClientSession] = None,
        debug_api : bool = False
    ) -> str:
        """
        updates internal attributes
        having an access_token assumes pre-authenticaiton
        """

        res = await test_access_token(
            domo_instance=self.domo_instance,
            domo_access_token=self.domo_access_token,
            session=session,
            debug_api = debug_api
        )

        if res.status == 401 and res.response == "Unauthorized":
            raise InvalidCredentialsError(
                status=res.status,
                message=res.response,
                domo_instance=self.domo_instance,
            )

        self.token = self.domo_access_token
        self.user_id = res.response.get("id")

        self.auth_header = self.generate_auth_header(token=self.token)

        if not self.token_name:
            self.token_name = "token_auth"

        return self.token

# %% ../../nbs/client/95_DomoAuth.ipynb 41
@dataclass
class _DomoDeveloperAuth_Required(_DomoAuth_Required):
    """mix requied parameters for DomoFullAuth"""

    domo_client_id: str
    domo_client_secret: str = field(repr=False)

# %% ../../nbs/client/95_DomoAuth.ipynb 42
@dataclass(init=False)
class DomoDeveloperAuth(_DomoAuth_Optional, _DomoDeveloperAuth_Required):
    """use for full authentication token"""

    def __init__(self, domo_client_id: str, domo_client_secret: str):
        self.domo_client_id = domo_client_id
        self.domo_client_secret = domo_client_secret
        self.domo_instance = ""

    def generate_auth_header(self, token: str) -> dict:
        self.auth_header = {"Authorization": "bearer " + token}
        return self.auth_header

    async def get_auth_token(
        self,
        session: Optional[aiohttp.ClientSession] = None,
        debug_api : bool = False
    ) -> str:

        res = await get_developer_auth(
            domo_client_id=self.domo_client_id,
            domo_client_secret=self.domo_client_secret,
            session=session,
            debug_api = debug_api
        )

        if res.status == 401:
            raise InvalidCredentialsError(
                status=res.status,
                message=str(res.response),
                domo_instance=self.domo_instance,
            )

        token = str(res.response.get("access_token"))
        self.token = token
        self.user_id = res.response.get("userId")
        self.domo_instance = res.response.get("domain")
        self.set_manual_login()

        self.auth_header = self.generate_auth_header(token=token)

        if not self.token_name:
            self.token_name = "developer_auth"

        return token
