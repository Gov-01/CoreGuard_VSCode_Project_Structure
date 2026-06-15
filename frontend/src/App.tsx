import { BrowserRouter, Routes, Route } from "react-router-dom";

import Dashboard from "./pages/Dashboard";
import EventDetails from "./pages/EventDetails";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/event/:id" element={<EventDetails />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;