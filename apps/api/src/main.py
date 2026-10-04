import uuid
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from src.api.auth import router
from src.core.config import settings
app = FastAPI(title="GATE AI Tutor API")
app.add_middleware(CORSMiddleware, allow_origins=[settings.web_origin], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
@app.middleware("http")
async def request_id(request: Request, call_next):
    rid = request.headers.get("x-request-id", str(uuid.uuid4()))[:128]
    response = await call_next(request)
    response.headers["X-Request-ID"] = rid
    return response
app.include_router(router)
@app.get("/health")
async def health(): return {"status": "ok"}
