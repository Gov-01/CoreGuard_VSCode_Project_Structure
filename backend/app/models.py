from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text

from app.database import Base


class Event(Base):

    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)

    supplier = Column(String)

    asset = Column(String)

    severity = Column(String)

    status = Column(String)

    owner = Column(String)

    summary = Column(String)

    source = Column(String)


class Note(Base):

    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)

    event_id = Column(Integer)

    note = Column(Text)
class AuditLog(Base):

    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, index=True)

    event_id = Column(Integer)

    field = Column(String)

    old_value = Column(String)

    new_value = Column(String)

    changed_by = Column(String)

    changed_at = Column(String)