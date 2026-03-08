import http from "k6/http";
import { check, sleep } from "k6";

const BASE_URL = __ENV.BASE_URL || "http://localhost:8000";

export const options = {
  stages: [
    { duration: "30s", target: 10 },
    { duration: "30s", target: 50 },
    { duration: "30s", target: 100 },
  ],
  gracefulRampDown: "10s",
};

export default function () {
  const res = http.get(`${BASE_URL}/health`);
  check(res, { "status 200": (r) => r.status === 200 });
  sleep(1);
}
