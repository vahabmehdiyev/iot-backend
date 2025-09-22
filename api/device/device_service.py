from sqlalchemy.ext.asyncio import AsyncSession
from .device_dao import list_devices

async def get_devices(db: AsyncSession) -> list[dict]:
    # Biznes qaydalarını sonra bura əlavə edəcəyik
    return await list_devices(db)