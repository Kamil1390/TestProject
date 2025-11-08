import uvicorn
from fastapi import FastAPI
from src.routers import router
from conf.config import CONFIG

app = FastAPI()
app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(app, host=CONFIG.host, port=CONFIG.port)
