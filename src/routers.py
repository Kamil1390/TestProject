from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException

from src.schemas import IncidentSchema, IncidentResponseSchema, IncidentID
from src.services import IncidentsDAO
from src.models import Status
from src.exceptions import NotFoundExceptions

router = APIRouter(prefix="", tags=["Incident"])


@router.post("/create", response_model=IncidentID)
async def create_incident(data: IncidentSchema):
    try:
        return await IncidentsDAO.create_incident(data)
    except Exception as er:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(er)
        )


@router.get("/get_incidents/{status_active}", response_model=list[IncidentResponseSchema])
async def git_info(status_active: Status):
    try:
        return await IncidentsDAO.get_list_incidents(status_active)
    except Exception as er:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(er)
        )

@router.patch("/update")
async def update_info(id_incident: int, status_active: Status) -> JSONResponse:
    try:
        return await IncidentsDAO.update_status(id_incident, status_active)
    except NotFoundExceptions as er:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(er)
        )
    except Exception as er:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(er)
        )
