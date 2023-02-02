import copy
from typing import IO, Any, Dict, Optional, Tuple, Union

import httpx
import pydantic
import uritemplate

from pydcapi import utils
from pydcapi.models import discovery_v1
from pydcapi.resources import (
    assets,
    connector,
    discovery,
    feedback,
    folders,
    jobs,
    operations,
    system,
    users,
)

_COMMON_HEADERS: Dict[str, str] = {
    "authority": "adobeid-na1.services.adobe.com",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8,ru;q=0.7",
    "dnt": "1",
    "origin": "https://acrobat.adobe.com",
    "referer": "https://acrobat.adobe.com/",
    "sec-ch-ua": '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "X-Requested-With": "XMLHttpRequest",
    "x-api-app-info": "dc-web-app",
    "x-api-client-id": "api_browser",
    "user-agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
    ),
}


class Credentials(pydantic.BaseModel):
    ims_sid: Optional[str]
    token: Optional[str]

    # noinspection PyMethodParameters
    @pydantic.root_validator
    def at_least_one_credential(
        cls, values: Dict[str, Any]  # noqa: N805 (actually a class method)
    ) -> Dict[str, Any]:
        if values.get("ims_sid") is None and values.get("token") is None:
            raise ValueError("ims_sid or token must be provided")
        return values


class Client:
    def __init__(self, *, credentials: Credentials) -> None:
        (self.__schema, self.__client) = self.__initialise(credentials)

        self.discovery = discovery.Discovery(self)
        self.folders = folders.Folders(self)
        self.users = users.Users(self)
        self.assets = assets.Assets(self)
        self.jobs = jobs.Jobs(self)
        self.operations = operations.Operations(self)
        self.system = system.System(self)
        self.feedback = feedback.Feedback(self)
        self.connector = connector.Connector(self)

    @classmethod
    def __initialise(
        cls, credentials: Credentials
    ) -> Tuple[discovery_v1.Model, httpx.Client]:
        token: Optional[str] = None
        schema: Optional[discovery_v1.Model] = None

        if credentials.token:
            token = credentials.token
            try:
                schema = cls.__initialise_schema(token=token)
            except httpx.HTTPError:
                token = None
            except Exception as ex:
                raise RuntimeError("failed to check token") from ex

        if not token:
            if not credentials.ims_sid:
                raise ValueError("ims_sid must be provided")

            try:
                token = credentials.token = cls.__refresh_token(credentials.ims_sid)
            except Exception as ex:
                raise RuntimeError("failed to refresh token") from ex

            try:
                schema = cls.__initialise_schema(token=token)
            except Exception as ex:
                raise RuntimeError("failed to refresh token") from ex

        client: httpx.Client = cls.__create_client(token=token)

        assert schema is not None
        assert client is not None

        return schema, client

    @staticmethod
    def __create_client(*, token: Optional[str]) -> httpx.Client:
        headers = copy.deepcopy(_COMMON_HEADERS)
        if token:
            headers["Authorization"] = f"Bearer {token}"

        return httpx.Client(headers=headers)

    @staticmethod
    def __initialise_schema(*, token: Optional[str]) -> discovery_v1.Model:
        with Client.__create_client(token=token) as client:
            resp = client.get(
                "https://dc-api.adobe.io/discovery",
                headers={"Accept": utils.content_type_from_model("discovery_v1")},
            )
            resp.raise_for_status()
            return discovery_v1.Model.parse_obj(resp.json())

    @staticmethod
    def __refresh_token(ims_sid: str) -> str:
        with Client.__create_client(token=None) as client:
            resp = client.post(
                "https://adobeid-na1.services.adobe.com/ims/check/v6/token",
                data={
                    "client_id": "dc-prod-virgoweb",
                    "scope": (
                        "AdobeID,openid,pydcapi,additional_info.account_type,additional_info.optionalAgreements,"
                        "agreement_sign,agreement_send,sign_library_write,sign_user_read,sign_user_write,"
                        "agreement_read,agreement_write,widget_read,widget_write,workflow_read,workflow_write,"
                        "sign_library_read,sign_user_login,sao.ACOM_ESIGN_TRIAL,ee.dcweb,tk_platform,tk_platform_sync,"
                        "ab.manage,additional_info.incomplete,additional_info.creation_source,"
                        "update_profile.first_name,update_profile.last_name",
                    ),
                },
                cookies={
                    "ims_sid": ims_sid,
                },
                params={"jslVersion": "v2-v0.38.0-17-g633319d"},
            )

            if not resp.is_success:
                raise RuntimeError(f"could not refresh token: {resp.text}")

            data = resp.json()
            token = data.get("access_token")
            if not token:
                raise RuntimeError(f"no token in response: {data}")

            return str(token)

    def request(
        self,
        *,
        method: str,
        url: str,
        content_type: Optional[str] = None,
        accept: Optional[str] = None,
        params: Optional[Dict[str, Union[int, str]]] = None,
        json: Optional[Any] = None,
        file: Optional[Union[IO[bytes], bytes, str]] = None,
        content: Optional[bytes] = None,
    ) -> httpx.Response:
        url = uritemplate.expand(
            url,
            base_url="https://dc-api.adobe.io",
            expiry=self.__schema.expiry,
        )

        headers = {}
        if accept:
            headers["Accept"] = accept
        if content_type:
            headers["Content-Type"] = content_type

        resp = self.__client.request(
            method,
            url,
            headers=headers,
            params=params,
            json=json,
            files={"file": file} if file else None,
            content=content,
        )

        try:
            resp.raise_for_status()
        except httpx.HTTPError as ex:
            raise RuntimeError(f"failed to request {method} {url}: {resp.text}") from ex
        return resp
