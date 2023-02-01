from pydantic import BaseModel, Field


class DatabaseConfig(BaseModel):
    url: str
    min_size: int = Field(default=0)
    max_size: int = Field(default=0)
