from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime

from app.database import SessionLocal
from app.models import Event, Note, AuditLog
from app.schemas import NoteRequest, AssignRequest
from app.dependencies import get_current_user

router = APIRouter()


@router.get("/events")
def get_events():
    db: Session = SessionLocal()
    events = db.query(Event).all()
    return events


@router.get("/events/{event_id}")
def get_event(event_id: int):
    db = SessionLocal()
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        return {"message": "Event Not Found"}
    return {
        "id": event.id,
        "supplier": event.supplier,
        "asset": event.asset,
        "severity": event.severity,
        "status": event.status,
        "owner": event.owner,
        "summary": event.summary,
        "source": event.source
    }


@router.post("/notes")
def add_note(data: NoteRequest):
    db = SessionLocal()
    note = Note(event_id=data.event_id, note=data.note)
    db.add(note)
    db.commit()
    return {"message": "Note Added"}


@router.get("/events/{event_id}/notes")
def get_notes(event_id: int):
    db = SessionLocal()
    notes = db.query(Note).filter(Note.event_id == event_id).all()
    result = []
    for n in notes:
        result.append({"id": n.id, "note": n.note})
    return result


@router.put("/events/{event_id}/assign")
def assign_event(event_id: int, data: AssignRequest, user=Depends(get_current_user)):
    if user.get("role") != "manager":
        return {"message": "Access Denied"}
    db = SessionLocal()
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        return {"message": "Event Not Found"}
    old_owner = event.owner
    event.owner = data.owner
    audit = AuditLog(
        event_id=event.id,
        field="owner",
        old_value=old_owner,
        new_value=data.owner,
        changed_by=user.get("sub"),
        changed_at=str(datetime.now())
    )
    db.add(audit)
    db.commit()
    return {"message": "Owner Assigned", "owner": event.owner}


@router.get("/summary")
def get_summary():
    db = SessionLocal()
    total_events = db.query(Event).count()
    high_count = db.query(Event).filter(Event.severity == "High").count()
    medium_count = db.query(Event).filter(Event.severity == "Medium").count()
    low_count = db.query(Event).filter(Event.severity == "Low").count()
    return {"total_events": total_events, "high": high_count, "medium": medium_count, "low": low_count}
