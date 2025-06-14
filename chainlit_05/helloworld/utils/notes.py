def save_note(text):
    with open("notes.txt", "a", encoding="utf-8") as f:
        f.write(text + "\n")
    return "✅ Note saved."

def list_notes():
    try:
        with open("notes.txt", "r", encoding="utf-8") as f:
            notes = f.readlines()
        return "📝 Your Notes:\n" + "".join(f"{i+1}. {n}" for i, n in enumerate(notes)) if notes else "No notes found."
    except FileNotFoundError:
        return "No notes file found."

def delete_note(index):
    try:
        with open("notes.txt", "r", encoding="utf-8") as f:
            notes = f.readlines()
        if 0 <= index-1 < len(notes):
            removed = notes.pop(index-1)
            with open("notes.txt", "w", encoding="utf-8") as f:
                f.writelines(notes)
            return f"🗑️ Deleted note: {removed.strip()}"
        return "Invalid note number."
    except FileNotFoundError:
        return "No notes to delete."
