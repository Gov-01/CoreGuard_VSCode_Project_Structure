import { useParams } from "react-router-dom";
import { useEffect, useState } from "react";
import { getEvent } from "../api/eventApi";

function EventDetails() {
  const { id } = useParams();

  const [event, setEvent] = useState<any>(null);

  useEffect(() => {
    loadEvent();
  }, []);

  const loadEvent = async () => {
    const data = await getEvent(id!);
    setEvent(data);
  };

  if (!event) {
    return <h2>Loading...</h2>;
  }

  return (
    <div style={{ padding: "30px" }}>
      <h1>Event Details</h1>

      <p>
        <strong>ID:</strong> {event.id}
      </p>

      <p>
        <strong>Supplier:</strong> {event.supplier}
      </p>

      <p>
        <strong>Asset:</strong> {event.asset}
      </p>

      <p>
        <strong>Severity:</strong> {event.severity}
      </p>

      <p>
        <strong>Status:</strong> {event.status}
      </p>

      <p>
        <strong>Owner:</strong> {event.owner}
      </p>

      <p>
        <strong>Summary:</strong> {event.summary}
      </p>

      <p>
        <strong>Source:</strong> {event.source}
      </p>
    </div>
  );
}

export default EventDetails;