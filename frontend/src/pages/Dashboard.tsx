import { useEffect, useState } from "react";
import { getSummary, getEvents } from "../api/eventApi";
import EventTable from "../components/EventTable";
import { useAuth } from "../auth/AuthContext";

function Dashboard() {

  const [summary, setSummary] = useState({
    total_events: 0,
    high: 0,
    medium: 0,
    low: 0,
  });
  const { role } = useAuth();
  const [events, setEvents] = useState<any[]>([]);

  const [search, setSearch] = useState("");

  useEffect(() => {
    loadData();
  }, []);

  const loadData = async () => {
  try {
    console.log("Loading API...");

    const summaryData = await getSummary();
    console.log("Summary:", summaryData);

    const eventsData = await getEvents();
    console.log("Events:", eventsData);

    setSummary(summaryData);
    setEvents(eventsData);
  } catch (err) {
    console.error("ERROR:", err);
  }
};

  const filteredEvents = events.filter(
    (event) =>
      (event.supplier || "")
        .toLowerCase()
        .includes(search.toLowerCase()) ||
      (event.asset || "")
        .toLowerCase()
        .includes(search.toLowerCase()) ||
      (event.owner || "")
        .toLowerCase()
        .includes(search.toLowerCase())
  );

  return (
  <div className="dashboard">
    <h1>Risk Review Console</h1>

    <div className="summary-cards">
      <div className="card">
        <h3>Total Events</h3>
        <p>{summary.total_events}</p>
      </div>

      <div className="card high">
        <h3>High</h3>
        <p>{summary.high}</p>
      </div>

      <div className="card medium">
        <h3>Medium</h3>
        <p>{summary.medium}</p>
      </div>

      <div className="card low">
        <h3>Low</h3>
        <p>{summary.low}</p>
      </div>
    </div>

    <div className="toolbar">
      <input
        type="text"
        placeholder="Search supplier, asset, owner..."
        value={search}
        onChange={(e) => setSearch(e.target.value)}
      />
    </div>

    <div className="events-header">
      <h2>Events</h2>

      {role === "manager" && (
        <button className="export-btn">
          Export Report
        </button>
      )}
    </div>

    <EventTable events={filteredEvents} />
  </div>
);
}

export default Dashboard;