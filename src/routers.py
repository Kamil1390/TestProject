from fastapi import APIRouter

router = APIRouter(prefix="/", tags=["Incident"])


@router.post("/create")
async def create_incident():
    pass


@router.get("/get_info")
async def git_info():
    pass


@router.put("/update")
async def update_info():
    pass
