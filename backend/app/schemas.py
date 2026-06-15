from pydantic import BaseModel


class EventResponse(BaseModel):
    id: int
    supplier: str | None = None
    asset: str | None = None
    severity: str | None = None
    status: str | None = None
    owner: str | None = None
    summary: str | None = None
    source: str | None = None

    class Config:
        orm_mode = True


class NoteRequest(BaseModel):
    event_id: int
    note: str


class NoteResponse(BaseModel):
    id: int
    event_id: int
    note: str

    class Config:
        orm_mode = True


class AssignRequest(BaseModel):
    owner: str


class SummaryResponse(BaseModel):
    total_events: int
    high: int
    medium: int
    low: int
