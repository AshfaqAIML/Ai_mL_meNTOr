import httpx

from app.config import LLM_API_KEY, LLM_API_URL, MODEL_NAME


async def call_llm(messages: list) -> str:
    """
    Calls an LLM API and returns the assistant reply.

    This is written for an OpenAI-compatible API format.
    If your provider is different, adjust this function.
    """

    if not LLM_API_URL:
        return (
            "LLM_API_URL is not set. "
            "Please add your LLM API URL in the .env file."
        )

    headers = {
        "Authorization": f"Bearer {LLM_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL_NAME,
        "messages": messages,
        "temperature": 0.4
    }

    async with httpx.AsyncClient(timeout=60.0) as client:
        response = await client.post(
            LLM_API_URL,
            headers=headers,
            json=payload
        )

        response.raise_for_status()
        data = response.json()

        return data["choices"][0]["message"]["content"]
