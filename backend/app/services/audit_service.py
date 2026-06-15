from app.models import AuditLog
from app.database import SessionLocal


def log_audit(event_id: int, field: str, old_value: str, new_value: str, changed_by: str):
    db = SessionLocal()
    audit = AuditLog(
        event_id=event_id,
        field=field,
        old_value=old_value,
        new_value=new_value,
        changed_by=changed_by,
        changed_at=""
    )
    db.add(audit)
    db.commit()
    return audit
