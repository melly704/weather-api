#!/bin/bash

uvicorn src.main:app --reload --port 8000 &
API_PID=$!
sleep 5

pytest src/tests
schemathesis run http://localhost:8000/openapi.json
locust -f locustfile.py --headless -u 10 -r 2 --run-time 20s --host http://localhost:8000

kill $API_PID
