from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from config.database import get_db
from .device_service import get_devices

router = APIRouter(prefix="/device", tags=["device"])

@router.get("/")
async def list_devices_endpoint(db: AsyncSession = Depends(get_db)):
    return await get_devices(db)
