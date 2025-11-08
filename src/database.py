from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from conf.config import BASE_DIR

engine = create_async_engine(
    f"aiosqlite:///{BASE_DIR}/data.db",
)
