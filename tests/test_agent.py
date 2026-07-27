import pytest
from unittest.mock import AsyncMock, patch

from app.schemas import UserProfile, Progress
from app import memory


def test_get_user_file():
    file_path = memory.get_user_file("test-user")
    assert file_path.name == "test-user.json"


def test_get_user_file_special_chars():
    file_path = memory.get_user_file("user@#$%name")
    assert file_path.name == "username.json"


def test_get_user_file_empty():
    file_path = memory.get_user_file("")
    assert file_path.name == "default.json"


def test_load_profile_default():
    profile = memory.load_profile("nonexistent_user_xyz")
    assert profile.user_id == "nonexistent_user_xyz"
    assert profile.name is None


def test_load_progress_default():
    progress = memory.load_progress("nonexistent_user_xyz")
    assert progress.completed_topics == []
    assert progress.next_topic == "Python basics"


def test_save_and_load_user():
    user_id = "test_save_load"
    profile = UserProfile(user_id=user_id, name="Test User", level="beginner")
    progress = Progress(next_topic="Python basics")

    memory.save_user(user_id, profile, progress)

    loaded_profile = memory.load_profile(user_id)
    loaded_progress = memory.load_progress(user_id)

    assert loaded_profile.name == "Test User"
    assert loaded_profile.level == "beginner"
    assert loaded_progress.next_topic == "Python basics"

    file_path = memory.get_user_file(user_id)
    file_path.unlink(missing_ok=True)


def test_limit_chat_history():
    progress = Progress()
    for i in range(25):
        progress.chat_history.append({"role": "user", "content": f"msg {i}"})

    memory.limit_chat_history(progress, max_messages=20)

    assert len(progress.chat_history) == 20
    assert progress.chat_history[0]["content"] == "msg 5"
    assert progress.chat_history[-1]["content"] == "msg 24"
