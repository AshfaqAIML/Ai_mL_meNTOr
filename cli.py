import asyncio

from app.agent import handle_message


async def main():
    user_id = "default"

    print("AI/ML Mentor started. Type 'exit' to quit.")

    while True:
        user_input = input("\nYou: ")

        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        reply, progress = await handle_message(user_id, user_input)

        print("\nAgent:", reply)


if __name__ == "__main__":
    asyncio.run(main())
