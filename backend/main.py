from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pyrasp.pyrasp import FastApiRASP
import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Setting up security system
#rasp = FastApiRASP(app, conf='rasp.json')

# Setting up CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Add the origin of your React frontend
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Authorization", "Content-Type"],
)

# Setting up InfluxDB configs

token = os.getenv('TOKEN')
org = "Threat-detection"
url = "http://localhost:8086"

influx_client = InfluxDBClient(url=url, token=token, org=org)

bucket="Threat-detection"

query_api = influx_client.query_api()

@app.get("/api/data")
async def get_data():
    try:
        query = """from(bucket: "Threat-detection")
        |> range(start: -10m)
        |> filter(fn: (r) => r._measurement == "measurement1")"""
        tables = query_api.query(query, org="Threat-detection")
        json_data = []
        for table in tables:
            for record in table.records:
                json_data.append(record)
        return json_data

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))