type Props = {
  severity: string;
  setSeverity: (value: string) => void;
};

function Filters({ severity, setSeverity }: Props) {
  return (
    <div className="filters">
      <select
        value={severity}
        onChange={(e) => setSeverity(e.target.value)}
      >
        <option value="">All Severity</option>
        <option value="Critical">Critical</option>
        <option value="High">High</option>
        <option value="Medium">Medium</option>
      </select>
    </div>
  );
}

export default Filters;