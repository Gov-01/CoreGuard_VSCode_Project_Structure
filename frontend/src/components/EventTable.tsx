import type { Event } from "../types/event";
import { useAuth } from "../auth/AuthContext";
import { Link } from "react-router-dom";

type Props = {
  events: Event[];
};

function EventTable({ events }: Props) {
  const { role } = useAuth();

  return (
    <table className="event-table">
      <thead>
        <tr>
          <th>ID</th>
          <th>Supplier</th>
          <th>Asset</th>
          <th>Severity</th>
          <th>Status</th>
          <th>Owner</th>
          <th>Actions</th>
        </tr>
      </thead>

      <tbody>
        {events.map((event) => (
          <tr key={event.id}>
            <td>
              <Link to={`/event/${event.id}`}>
                {event.id}
              </Link>
            </td>

            <td>{event.supplier}</td>

            <td>{event.asset}</td>

            <td>
              <span
                className={`severity ${event.severity.toLowerCase()}`}
              >
                {event.severity}
              </span>
            </td>

            <td>{event.status}</td>

            <td>{event.owner}</td>

            <td>
              {role === "manager" ? (
                <button className="edit-btn">
                  Edit
                </button>
              ) : (
                "-"
              )}
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default EventTable;