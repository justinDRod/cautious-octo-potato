import json
from geopy.geocoders import Nominatim
from geopy.distance import geodesic as measure
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

locations = []
geolocator = Nominatim(user_agent="Distance comparison")

origins = [
    "http://localhost",
    "http://localhost:8000",
    "https://justindrod.github.io",
]

# I added this special function which lets us read data from the database file 
# when the application first starts. Then we assign it to a variable and use
# that variable each time.

# The reason for this is opening and reading from files is an operation which takes time (relatively
# since computers are so fast) so instead of opening the file each time we call the api, we just 
# do it once when the app starts up
@asynccontextmanager
async def lifespan(app: FastAPI):
    global locations
    # Using relative file path syntax so it is not specific to your computer and can run on servers
    with open("app/resources/locations.json", "r") as f:
      locations = locations + json.load(f)
      yield

app = FastAPI(lifespan=lifespan)

# this code allows us to call the api from web pages. This will come up again and again if you get into web development
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def root(address: str):
    #gathers location from user and gets cords
    print("Using Address: " + address)
    Clocation = address
    x = geolocator.geocode(Clocation)
    Clocation = (x.latitude, x.longitude) 

    #defining variables
    llist = []
    dictionary = {}
    list_of_place=[]
    list_of_dist=[]
    y=0

    #Mesures distance from json parameters
    for location in locations:
        cords = (location["lat"],location["Long"])
        place = (location["name"])
        distance_location_sl = (measure(cords,Clocation).miles)
        dictionary[place]= distance_location_sl
        llist.append({"distance": distance_location_sl,
                         "place": place })
    return llist
