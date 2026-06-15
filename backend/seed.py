from app.database import SessionLocal
from app.models import Event

db = SessionLocal()

event1 = Event(
    supplier="Dell",
    asset="Laptop",
    severity="Critical",
    status="New",
    owner="John",
    summary="Malware detected",
    source="CrowdStrike"
)

event2 = Event(
    supplier="Cisco",
    asset="Router",
    severity="High",
    status="Reviewed",
    owner="Alice",
    summary="Configuration issue",
    source="SIEM"
)

event3 = Event(
    supplier="AWS",
    asset="Cloud Server",
    severity="Medium",
    status="Escalated",
    owner="David",
    summary="Suspicious traffic",
    source="GuardDuty"
)

db.add(event1)
db.add(event2)
db.add(event3)

db.commit()

print("Seed Data Added Successfully")