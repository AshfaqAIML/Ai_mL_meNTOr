import json
from pathlib import Path

from app.config import USERS_DIR
from app.schemas import UserProfile, Progress


def get_user_file(user_id: str) -> Path:
    safe_name = "".join(
        c for c in user_id if c.isalnum() or c in ("-", "_")
    ) or "default"

    return USERS_DIR / f"{safe_name}.json"


def load_profile(user_id: str) -> UserProfile:
    file_path = get_user_file(user_id)

    if file_path.exists():
        data = json.loads(file_path.read_text(encoding="utf-8"))
        profile_data = data.get("profile", {})
        return UserProfile(**profile_data)

    return UserProfile(user_id=user_id)


def load_progress(user_id: str) -> Progress:
    file_path = get_user_file(user_id)

    if file_path.exists():
        data = json.loads(file_path.read_text(encoding="utf-8"))
        progress_data = data.get("progress", {})
        return Progress(**progress_data)

    return Progress()


def save_user(user_id: str, profile: UserProfile, progress: Progress):
    file_path = get_user_file(user_id)

    data = {
        "profile": profile.model_dump(),
        "progress": progress.model_dump()
    }

    file_path.write_text(
        json.dumps(data, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )


def limit_chat_history(progress: Progress, max_messages: int = 20):
    progress.chat_history = progress.chat_history[-max_messages:]
