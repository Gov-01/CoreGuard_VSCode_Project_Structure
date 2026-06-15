import { createContext, useContext, useState } from "react";

type Role = "manager" | "operator";

interface AuthContextType {
  role: Role;
  setRole: (role: Role) => void;
}

const AuthContext = createContext<AuthContextType>({
  role: "operator",
  setRole: () => {},
});

export const AuthProvider = ({ children }: any) => {
  const [role, setRole] = useState<Role>("operator");

  return (
    <AuthContext.Provider value={{ role, setRole }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => useContext(AuthContext);