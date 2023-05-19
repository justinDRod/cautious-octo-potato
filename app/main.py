import json
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

locations = []
origins = [
    "http://localhost",
    "http://localhost:8080",
    "https://justindrod.github.io",
]

@asynccontextmanager
async def lifespan(app: FastAPI):
    global locations
    with open("app/resources/locations.json", "r") as f:
      locations = locations + json.load(f)
      yield

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def root(address: str):
    return locations
