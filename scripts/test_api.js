import http from 'k6/http';
import { check, sleep } from "k6";

const isNumeric = (value) => /^\d+$/.test(value);

const default_vus = 100; //Virtual Users
const endpoint = 'https://httpbin.test.k6.io/post' // Endpoint to test


const target_vus_env = `${__ENV.TARGET_VUS}`;
const target_vus = isNumeric(target_vus_env) ? Number(target_vus_env) : default_vus;

// test type
export let options = {

  stages: [
    // Ramp-up from 1 to TARGET_VUS virtual users (VUs) in 5s
    { duration: "5s", target: target_vus },

    // Stay at rest on TARGET_VUS VUs for 10s
    { duration: "30s", target: target_vus },

    // Ramp-down from TARGET_VUS to 0 VUs for 5s
    { duration: "5s", target: 0 }
  ]
};

export default function () {

  const payload = JSON.stringify({
    name: 'lorem',
    surname: 'ipsum',
  });
  const headers = { 'Content-Type': 'application/json' };
  const response = http.post(endpoint, payload, { headers });
  check(response, { "status is 200": (r) => r.status === 200 });
  sleep(.300);
};
