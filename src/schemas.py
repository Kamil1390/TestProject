from enum import Enum
from pydantic import BaseModel

class Status(str, Enum):
    active = "active"
    dont_active = "dont_active"

class IncidentSchema(BaseModel):
    description: str
    status: Status
    source: str
