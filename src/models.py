import enum
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, DateTime, Enum, func
from database import Base


class Status(enum.Enum):
    active = "active"
    dont_active = "dont_active"


class Incident(Base):
    __tablename__ = "incedents"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    description: Mapped[str] = mapped_column(DateTime, nullable=False)
    status: Mapped[Status] = mapped_column(Enum(Status), nullable=False)
    source: Mapped[str] = mapped_column(String, nullable=False)
    daterecord: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
