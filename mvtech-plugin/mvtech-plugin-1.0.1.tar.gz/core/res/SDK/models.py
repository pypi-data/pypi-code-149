from pydantic import BaseModel
"""
插件标准入参
"""


class PLUGIN_BASE_MODEL(BaseModel):
    version: str
    type: str
    body: dict
