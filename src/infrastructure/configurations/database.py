from abc import abstractmethod

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from src.infrastructure.configurations.environments import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


class BaseModel(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)

    @abstractmethod
    def to_read_model(self):
        raise NotImplementedError


async def get_async_session() -> AsyncSession:
    async with async_session_maker() as session:
        yield session
