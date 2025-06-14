from datetime import datetime, timedelta
from utils.calendar_auth import get_calendar_service

def create_event(summary, description, start_time_str, duration_minutes=30):
    service = get_calendar_service()
    start_time = datetime.strptime(start_time_str, "%Y-%m-%d %H:%M")
    end_time = start_time + timedelta(minutes=duration_minutes)

    event = service.events().insert(calendarId='primary', body={
        "summary": summary,
        "description": description,
        "start": {"dateTime": start_time.isoformat(), "timeZone": "Asia/Karachi"},
        "end": {"dateTime": end_time.isoformat(), "timeZone": "Asia/Karachi"},
    }).execute()

    return f"📅 Event created: {event.get('htmlLink')}"
