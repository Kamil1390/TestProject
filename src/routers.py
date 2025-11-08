from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException

from src.schemas import IncidentSchema
from src.services import IncidentsDAO
from src.models import Status

router = APIRouter(prefix="", tags=["Incident"])


@router.post("/create")
async def create_incident(data: IncidentSchema):
    try:
        return await IncidentsDAO.create_incident(data)
    except Exception as er:
        print("error:", er)


@router.get("/get_incidents/{status_active}")
async def git_info(status_active: Status):
    try:
        return await IncidentsDAO.get_list_incidents(status_active)
    except Exception as er:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(er)
        )

@router.patch("/update")
async def update_info(id_incident: int, status_active: str):
    try:
        return await IncidentsDAO.update_status(id_incident, status_active)
    except Exception as er:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(er)
        )
