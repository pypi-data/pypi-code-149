""" Object relational mapper models
    Authors: Joshoua Bigler

    Description
    -----------
    Module contains models for the Steinemann DPE IoT SQL databases.
"""

from datetime import datetime
from typing import Optional, List

from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import Column, DateTime
from pydantic import condecimal


class JobStatistics(SQLModel, table=True):
  """Class for creating job entries into job stories table"""

  id: Optional[int] = Field(default=None, primary_key=True)
  machineId: str
  jobName: str
  jobSize: int
  productivity: condecimal(max_digits=4, decimal_places=3)
  waste: condecimal(max_digits=4, decimal_places=3)
  temperature: condecimal(max_digits=5, decimal_places=2)
  humidity: condecimal(max_digits=5, decimal_places=2)
  jobStart: datetime = Field(sa_column=Column(DateTime(timezone=False)), nullable=False)
  jobEnd: datetime = Field(sa_column=Column(DateTime(timezone=False)), nullable=False)
  productionTime: int


class Metrics(SQLModel, table=True):
  """Class for working with the metrics table"""

  id: Optional[int] = Field(default=None, primary_key=True)
  metricIdentifier: str = Field(index=True)
  machineId: str = Field(foreign_key='machines.id')
  displayName: str
  unit: str
  metricType: str
  numerics: List['NumericMeasurementValues'] = Relationship(back_populates='metric')


class NumericMeasurementValues(SQLModel, table=True):
  """Class for working with the numericMeasurementValues table"""

  machineId: int = Field(unique=False, primary_key=True, foreign_key='machines.id')
  metricId: int = Field(unique=False, primary_key=True, foreign_key='metrics.id')
  timestamp: datetime = Field(default_factory=datetime.utcnow, nullable=False)
  ingestionTimestamp: datetime = Field(default_factory=datetime.utcnow, nullable=False)
  value: float
  metric: List[Metrics] = Relationship(back_populates='numerics')


class TextMeasurementValues(SQLModel, table=True):
  """Class for working with the textMeasurementValues table"""

  machineId: int = Field(unique=False, primary_key=True, foreign_key='machines.id')
  metricId: int = Field(unique=False, primary_key=True, foreign_key='metrics.id')
  timestamp: datetime = Field(default_factory=datetime.utcnow, nullable=False)
  ingestionTimestamp: datetime = Field(default_factory=datetime.utcnow, nullable=False)
  value: str


class Machines(SQLModel, table=True):
  """Class for working with the machines table"""

  id: Optional[int] = Field(default=None, primary_key=True)
  machineIdentifier: str
  long: Optional[condecimal(max_digits=9, decimal_places=6)]
  lat: Optional[condecimal(max_digits=8, decimal_places=6)]
  city: Optional[str]
  country: Optional[str]
  description: str
  machineType: Optional[str]


class View_TableauNumericMeasurementValues(SQLModel, table=True):
  """Class for working with the view_TableauNumericMeasurementValues table"""

  machineId: int = Field(unique=False, primary_key=True, foreign_key='machines.id')
  metricId: int = Field(unique=False, primary_key=True, foreign_key='metrics.id')
  timestampLocal: datetime
  timestampUtc: datetime = Field(default_factory=datetime.utcnow, nullable=False)
  value: float


class View_TableauTextMeasurementValues(SQLModel, table=True):
  """Class for working with the view_TableauTextMeasurementValues table"""

  machineId: int = Field(unique=False, primary_key=True, foreign_key='machines.id')
  metricId: int = Field(unique=False, primary_key=True, foreign_key='metrics.id')
  timestampLocal: datetime
  timestampUtc: datetime = Field(default_factory=datetime.utcnow, nullable=False)
  value: str


class Tenants(SQLModel, table=True):
  """Class for working with the tenants table"""

  id: Optional[int] = Field(default=None, primary_key=True)
  tenantIdentifier: str
  description: Optional[str]
  long: Optional[condecimal(max_digits=9, decimal_places=6)]
  lat: Optional[condecimal(max_digits=8, decimal_places=6)]
  city: Optional[str]
  country: Optional[str]
  onboardingState: Optional[str]
