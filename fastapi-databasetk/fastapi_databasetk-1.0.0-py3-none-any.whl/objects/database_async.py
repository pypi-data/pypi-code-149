from fastapi import FastAPI
from databases import Database
from starlette.requests import Request
from .base import DatabaseBase


class AsyncDatabase(DatabaseBase):
    def database(self) -> Database:
        config = self.config
        url = config.url
        min_size = config.min_size
        max_size = config.max_size
        return Database(url, min_size=min_size, max_size=max_size)

    def database_from_starlette_request(self, request: Request) -> Database:
        return request.app.state._db

    def attach_to_fastapi_app(self, app: FastAPI):
        async def startup() -> None:
            db = self.database()
            try:
                await db.connect()
                app.state._db = db
            except Exception as error:
                print(error)

        async def shutdown() -> None:
            try:
                await app.state._db.disconnect()
            except Exception as error:
                print(error)

        app.add_event_handler("startup", startup)
        app.add_event_handler("shutdown", shutdown)
