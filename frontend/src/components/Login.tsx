import { useAuth } from "../auth/AuthContext";

function Login() {
  const { role, setRole } = useAuth();

  return (
    <div className="role-switch">
      <h3>User Role</h3>

      <select
        value={role}
        onChange={(e) =>
          setRole(e.target.value as "manager" | "operator")
        }
      >
        <option value="operator">Operator</option>
        <option value="manager">Manager</option>
      </select>
    </div>
  );
}

export default Login;