from sqlalchemy import select
from fastapi import status
from src.database import session_maker
from src.models import Incident
from src.schemas import IncidentSchema
from fastapi.responses import JSONResponse

class IncidentsDAO:
    @classmethod
    async def get_list_incidents(cls, status_active: str):
        async with session_maker() as session:
            stmt = select(Incident).where(Incident.status==status_active)
            result = await session.execute(stmt)
            return result.mappings().all()

    @classmethod
    async def create_incident(cls, data: IncidentSchema) -> JSONResponse:
        async with session_maker() as session:
            incident = Incident(**data.model_dump())
            session.add(incident)
            await session.commit()
            return JSONResponse(
                status_code=status.HTTP_204_NO_CONTENT,
                content={"detail": "incident created"}
            )

    @classmethod
    async def update_status(cls, id_incident: int, status_active: str) -> JSONResponse:
        async with session_maker() as session:
            incident = await session.get(Incident, id_incident)
            if not incident:
                return JSONResponse(
                    status_code=404,
                    content={"detail": "incident not found"}
            )
            incident.status = status_active
            await session.commit()
            return JSONResponse(
                status_code=204,
                content={"detail": "status updated"}
            )
