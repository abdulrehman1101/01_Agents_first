import os
from dotenv import load_dotenv
from utils.calendar_event import create_event
from utils.notes import save_note, list_notes, delete_note
from utils.tasks import add_task, list_tasks, delete_task
# from utils.voice import speak
from litellm import acompletion  

load_dotenv()

GEMINI_MODEL = "gemini/gemini-2.0-flash" 
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")  

async def handle_user_input(user_input: str) -> str:
    lower = user_input.lower()

    if lower.startswith("create event"):
        try:
            parts = user_input.split(" on ")
            title = parts[0].replace("create event", "").strip()
            time = parts[1].strip()
            return create_event(title, "Created via assistant", time)
        except:
            return "⚠️ Format: create event Meeting on 2025-06-15 15:00"

    elif lower.startswith("save note"):
        return save_note(user_input[len("save note"):].strip())

    elif lower.startswith("list notes"):
        return list_notes()

    elif lower.startswith("delete note"):
        try:
            return delete_note(int(user_input.split()[-1]))
        except:
            return "⚠️ Format: delete note 1"

    elif lower.startswith("add task"):
        return add_task(user_input[len("add task"):].strip())

    elif lower.startswith("list tasks"):
        return list_tasks()

    elif lower.startswith("delete task"):
        try:
            return delete_task(int(user_input.split()[-1]))
        except:
            return "⚠️ Format: delete task 1"

    else:
        try:
            response = await acompletion(
                model=GEMINI_MODEL,
                messages=[{"role": "user", "content": user_input}],
                api_key=GOOGLE_API_KEY
            )
            reply = response['choices'][0]['message']['content']
            return reply
        except Exception as e:
            return f"❌ Gemini API Error: {e}"
