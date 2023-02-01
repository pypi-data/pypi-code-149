from abc import abstractmethod
from pydantic import BaseModel
from databases import Database
from fastapi import FastAPI
from starlette.requests import Request
from .config import DatabaseConfig


class DatabaseBase(BaseModel):
    config: DatabaseConfig

    @abstractmethod
    def database(self) -> Database:
        pass

    @abstractmethod
    def attach_to_fastapi_app(self, app: FastAPI):
        pass

    @abstractmethod
    def database_from_starlette_request(self, request: Request) -> Database:
        pass
