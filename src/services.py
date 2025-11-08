from sqlalchemy import select, insert
from fastapi import status
from fastapi.responses import JSONResponse

from src.database import session_maker
from src.models import Incident
from src.schemas import IncidentSchema, IncidentResponseSchema, IncidentID
from src.exceptions import NotFoundExceptions

class IncidentsDAO:
    @classmethod
    async def get_list_incidents(cls, status_active: str) -> list[IncidentResponseSchema]:
        async with session_maker() as session:
            stmt = select(Incident).where(Incident.status==status_active)
            result = await session.execute(stmt)
            return result.scalars().all()

    @classmethod
    async def create_incident(cls, data: IncidentSchema) -> IncidentID:
        async with session_maker() as session:
            stmt = (
                insert(Incident)
                .values(**data.model_dump())
                .returning(Incident.id)
            )
            result = await session.execute(stmt)
            await session.commit()
            result = result.first()
            return IncidentID(id=result[0])

    @classmethod
    async def update_status(cls, id_incident: int, status_active: str) -> JSONResponse:
        async with session_maker() as session:
            incident = await session.get(Incident, id_incident)
            if not incident:
                raise NotFoundExceptions("Incident not found")
            incident.status = status_active
            await session.commit()
            return JSONResponse(
                status_code=200,
                content={"detail": "status updated"}
            )
