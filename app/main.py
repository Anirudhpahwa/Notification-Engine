from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.dependencies import get_db
from core.database import engine, Base
from schemas.common import HealthCheckResponse


app = FastAPI(
    title="Notification Engine",
    description="Event-driven notification system",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup():
    """Create database tables on startup."""
    Base.metadata.create_all(bind=engine)


@app.get("/", response_model=HealthCheckResponse)
async def root():
    """Root endpoint."""
    return HealthCheckResponse(status="ok", service="notification-engine")


@app.get("/health", response_model=HealthCheckResponse)
async def health_check():
    """Health check endpoint."""
    return HealthCheckResponse(status="healthy", service="notification-engine")