from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from database.config import settings
from sqlalchemy.orm import DeclarativeBase
from typing import Annotated
from sqlalchemy.orm import mapped_column

async_engine = create_async_engine(
    url=settings.database_url_asyncpg,
    echo=True,
)

async_session_factory = async_sessionmaker(async_engine)


class Base(DeclarativeBase):
    pass

intpk = Annotated[int, mapped_column(primary_key=True)]