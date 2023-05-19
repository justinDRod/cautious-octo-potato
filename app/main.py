import json
from contextlib import asynccontextmanager
from fastapi import FastAPI

locations = []

@asynccontextmanager
async def lifespan(app: FastAPI):
    with open("app/resources/locations.json", "r") as f:
      locations.append(json.load(f))
      yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
def root(address: str):
    print(locations)
    return {"message": "Hello, " + address + "!!!"}
