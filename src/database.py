from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from conf.config import BASE_DIR

DB_URL = f"sqlite+aiosqlite:///{BASE_DIR}/data.db"

engine = create_async_engine(DB_URL)

session_maker = async_sessionmaker(engine)

class Base(DeclarativeBase):
    pass
