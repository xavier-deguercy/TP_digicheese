import http from "k6/http";
import { check, sleep } from "k6";

const BASE_URL = __ENV.BASE_URL || "http://localhost:8000";

export const options = {
  vus: 10,
  duration: "10s",
};

export default function () {
  const res = http.get(`${BASE_URL}/health`);
  check(res, { "status 200": (r) => r.status === 200 });
  sleep(1);
}
