from fastapi import APIRouter

from app import memory
from app.schemas import UserProfile, Progress

router = APIRouter()


@router.get("/progress/{user_id}", response_model=Progress)
def get_progress(user_id: str):
    return memory.load_progress(user_id)


@router.get("/profile/{user_id}", response_model=UserProfile)
def get_profile(user_id: str):
    return memory.load_profile(user_id)


@router.post("/profile/{user_id}")
def update_profile(user_id: str, profile: UserProfile):
    progress = memory.load_progress(user_id)

    profile.user_id = user_id
    memory.save_user(user_id, profile, progress)

    return {
        "status": "saved",
        "profile": profile
    }
