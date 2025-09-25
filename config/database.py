from collections.abc import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

DATABASE_URL = "postgresql+asyncpg://app_user:merdekan454@127.0.0.1:55432/iotdb"
    # DATABASE_URL = "postgresql+asyncpg://app_user:merdekan454@127.0.0.1:5432/iotdb"

engine = create_async_engine(DATABASE_URL, echo=True)

SessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,        # (class_ opsionaldır, amma əlavə etmək olar)
    expire_on_commit=False,
    autoflush=False,
)

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as session:
        yield session
