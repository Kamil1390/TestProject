from enum import Enum
from datetime import datetime
from pydantic import BaseModel

class Status(str, Enum):
    active = "active"
    dont_active = "dont_active"

class IncidentID(BaseModel):
    id: int

class IncidentSchema(BaseModel):
    description: str
    status: Status
    source: str

class IncidentResponseSchema(BaseModel):
    id: int
    description: str
    status: str
    source: str
    daterecord: datetime
