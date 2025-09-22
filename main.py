from fastapi import FastAPI
from api.device.device_view import router as device_router

app = FastAPI(title="IoT Backend", version="0.1.0")

@app.get("/health")
async def health():
    return {"ok": True}

# device router-i əlavə edirik
app.include_router(device_router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=False
    )
