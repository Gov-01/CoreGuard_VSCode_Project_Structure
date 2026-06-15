import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

export const getSummary = async () => {
  const response = await API.get("/summary");
  return response.data;
};

export const getEvents = async () => {
  const response = await API.get("/events");
  return response.data;
};
export const getEvent = async (id: string) => {
  const response = await axios.get(
    `http://127.0.0.1:8000/events/${id}`
  );

  return response.data;
};