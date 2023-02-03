from pydantic import BaseModel
from typing import Optional


class DepartmentsParams(BaseModel):
    nom: Optional[str]
    limit: Optional[int]


class DepartmentCodeParams(BaseModel):
    code: Optional[str]
    limit: Optional[int]


class RegionDepartmentCodeParams(BaseModel):
    regioncode: Optional[str]
    limit: Optional[int]

# results ( everything optional in order to avoid mistakes)


class Department(BaseModel):
    nom: Optional[str]
    code: Optional[str]
    codeRegion: Optional[str]


class RegionsParams(DepartmentsParams):
    pass


class RegionCodeParams(DepartmentCodeParams):
    pass


class Region(BaseModel):
    nom: Optional[str]
    code: Optional[str]


class DepartmentsResponse(BaseModel):

    nom: str
    code: int
    codeRegion: int
    _score: Optional[float]
