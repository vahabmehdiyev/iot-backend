from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from .device_model import Device

async def list_devices(db: AsyncSession) -> list[dict]:
    stmt = select(
        Device.id, Device.name, Device.description, Device.created_at
    ).order_by(Device.id.asc())
    rows = (await db.execute(stmt)).mappings().all()
    return [dict(r) for r in rows]
