from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.middleware.timer import timing_middleware
from app.routes.auth import router as auth_router
from app.routes.issues import router as issues_router

app = FastAPI(
    title="Issue Tracker API",
    version="0.1.0",
    description="Issue Tracker API built with FastAPI",
)

app.middleware("http")(timing_middleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.get("/health")


def health_check():
    return {"status": "ok"}


app.include_router(auth_router)
app.include_router(issues_router)
