from databases import Database
from fastapi import FastAPI
from starlette.requests import Request
from .base import DatabaseBase


class SyncDatabase(DatabaseBase):
    def database(self) -> Database:
        return Database(self.config.url)

    def database_from_starlette_request(self, request: Request) -> Database:
        return request.app.state._db

    def attach_to_fastapi_app(self, app: FastAPI):
        def startup() -> None:
            db = self.database()
            try:
                db.connect()
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
