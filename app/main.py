from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import chat, progress

app = FastAPI(
    title="AI/ML Mentor Agent",
    description="A Python agent that teaches AI and ML engineering",
    version="1.0.0"
)

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat.router)
app.include_router(progress.router)


@app.get("/")
def home():
    return {
        "message": "AI/ML Mentor Agent is running"
    }
