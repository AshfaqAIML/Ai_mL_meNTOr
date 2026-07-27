from app.schemas import UserProfile, Progress
from app.curriculum import get_curriculum_text


SYSTEM_PROMPT = """
You are AI/ML Mentor, a friendly and practical personal tutor for AI and Machine Learning engineering.

Your goal is to help the user learn AI/ML step by step.

Teaching rules:
1. Use simple English.
2. Teach one topic at a time.
3. Give examples.
4. Give small exercises.
5. Check understanding.
6. Be patient and encouraging.
7. Do not overwhelm the user.
8. If the user is wrong, correct them gently.
9. Prefer step-by-step guidance.
10. Suggest projects when useful.
11. If the user wants a job, prepare them with projects and interview practice.
12. Do not give direct assignment answers for submission. Instead, guide them.

You can help with:
- roadmap creation
- lessons
- quizzes
- exercises
- code review
- project guidance
- interview preparation
- revision

Always adapt to the user's level and goal.
"""


def build_context(profile: UserProfile, progress: Progress) -> str:
    curriculum_text = get_curriculum_text()

    context = f"""
Current user profile:
- Name: {profile.name or "Unknown"}
- Level: {profile.level or "Unknown"}
- Python level: {profile.python_level or "Unknown"}
- Math level: {profile.math_level or "Unknown"}
- Daily study time: {profile.daily_time or "Unknown"}
- Goal: {profile.goal or "Unknown"}

Current progress:
- Completed topics: {", ".join(progress.completed_topics) if progress.completed_topics else "None"}
- Weak areas: {", ".join(progress.weak_areas) if progress.weak_areas else "None"}
- Current topic: {progress.current_topic or "None"}
- Next topic: {progress.next_topic or "None"}

Available curriculum:
{curriculum_text}
"""

    return context


def build_messages(profile: UserProfile, progress: Progress, user_message: str):
    system_content = SYSTEM_PROMPT + "\n" + build_context(profile, progress)

    messages = [
        {
            "role": "system",
            "content": system_content
        }
    ]

    messages.extend(progress.chat_history[-10:])

    messages.append(
        {
            "role": "user",
            "content": user_message
        }
    )

    return messages
