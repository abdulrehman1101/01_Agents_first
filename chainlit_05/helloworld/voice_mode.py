from assistant import handle_user_input
from utils.voice import listen, speak
import asyncio

async def voice_loop():
    while True:
        query = listen()
        if "exit" in query.lower():
            speak("Goodbye!")
            break
        response = await handle_user_input(query)
        speak(response)

if __name__ == "__main__":
    asyncio.run(voice_loop())
