import json, os

TASKS_FILE = "tasks.json"

def load_tasks():
    return json.load(open(TASKS_FILE)) if os.path.exists(TASKS_FILE) else []

def save_tasks(tasks):
    json.dump(tasks, open(TASKS_FILE, "w", encoding="utf-8"), indent=2)

def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    return "✅ Task added."

def list_tasks():
    tasks = load_tasks()
    return "📋 Your Tasks:\n" + "\n".join(f"{i+1}. {t}" for i, t in enumerate(tasks)) if tasks else "No tasks found."

def delete_task(index):
    tasks = load_tasks()
    if 0 <= index-1 < len(tasks):
        removed = tasks.pop(index-1)
        save_tasks(tasks)
        return f"🗑️ Deleted task: {removed}"
    return "❌ Invalid task number."
