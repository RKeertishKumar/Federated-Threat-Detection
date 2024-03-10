from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pyrasp.pyrasp import FastApiRASP

app = FastAPI()

# Setting up security system
rasp = FastApiRASP(app, conf='rasp.json')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Add the origin of your React frontend
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Authorization", "Content-Type"],
)

@app.get("/api/data")
def get_data():
    return "Hello, world"