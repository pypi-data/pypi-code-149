import json
from typing import Optional

from ai_openchat.aiiohttp import AiohttpSession
from ai_openchat.base.model import Model
from ai_openchat.base.session import BaseSession
from ai_openchat.utils.token import validate_token


class AsyncOpenAI:
    def __init__(self, token: str, session: Optional[BaseSession] = None) -> None:

        validate_token(token)

        if session is None:
            session = AiohttpSession()

        self.session = session
        self.__token = token

    @property
    def token(self) -> str:
        return self.__token

    async def send_message(self, message, model: Model):
        session = await self.session.create_session()
        url = self.session.api.api_url()
        headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + self.__token}
        model.prompt = message

        payload = json.dumps(model.__dict__)

        try:
            async with session.post(url, data=payload, headers=headers) as resp:
                return await resp.json()
        finally:
            await session.close()
