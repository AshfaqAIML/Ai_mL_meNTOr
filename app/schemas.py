from typing import List, Optional
from pydantic import BaseModel, Field


class UserProfile(BaseModel):
    user_id: str = "default"
    name: Optional[str] = None
    level: Optional[str] = None
    python_level: Optional[str] = None
    math_level: Optional[str] = None
    daily_time: Optional[str] = None
    goal: Optional[str] = None


class Progress(BaseModel):
    completed_topics: List[str] = Field(default_factory=list)
    weak_areas: List[str] = Field(default_factory=list)
    current_topic: Optional[str] = None
    next_topic: Optional[str] = "Python basics"
    chat_history: List[dict] = Field(default_factory=list)


class ChatRequest(BaseModel):
    user_id: str = "default"
    message: str


class ChatResponse(BaseModel):
    user_id: str
    reply: str
    progress: Progress
