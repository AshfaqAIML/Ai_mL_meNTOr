from app import memory, prompts, llm
from app.schemas import Progress


async def handle_message(user_id: str, message: str) -> tuple[str, Progress]:
    profile = memory.load_profile(user_id)
    progress = memory.load_progress(user_id)

    messages = prompts.build_messages(profile, progress, message)

    reply = await llm.call_llm(messages)

    progress.chat_history.append(
        {
            "role": "user",
            "content": message
        }
    )

    progress.chat_history.append(
        {
            "role": "assistant",
            "content": reply
        }
    )

    memory.limit_chat_history(progress, max_messages=20)

    memory.save_user(user_id, profile, progress)

    return reply, progress
