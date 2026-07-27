from fastapi import APIRouter

from app.schemas import ChatRequest, ChatResponse
from app.agent import handle_message

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    reply, progress = await handle_message(
        user_id=request.user_id,
        message=request.message
    )

    return ChatResponse(
        user_id=request.user_id,
        reply=reply,
        progress=progress
    )
