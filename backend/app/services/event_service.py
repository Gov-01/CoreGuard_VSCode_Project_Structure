from typing import List
from app.models import Event, Note
from app.database import SessionLocal


def get_events() -> List[Event]:
    db = SessionLocal()
    return db.query(Event).all()


def get_event_by_id(event_id: int) -> Event | None:
    db = SessionLocal()
    return db.query(Event).filter(Event.id == event_id).first()


def add_note(event_id: int, note_text: str):
    db = SessionLocal()
    note = Note(event_id=event_id, note=note_text)
    db.add(note)
    db.commit()
    return note
