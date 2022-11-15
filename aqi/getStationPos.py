
from geopy.geocoders import Nominatim
import pandas as pd
import numpy as np

### Station Headers ###
#   0:  stationName
#   1:  stationID

stations = pd.read_csv('aqi/output-data/stations.csv').to_numpy()
geolocator = Nominatim(user_agent='geopy test')

stationNames = stations[0]
stationIDs = stations[1]

stationPos = {}
for station in stationNames:
    location = geolocator.geocode(station)
    try:
        print((location.latitude, location.longitude))
    except:
        stationPos[station] = {"lat": {17.751983}, "lon": {-62.955379}}
    else:
        stationPos[station] = {"lat": {location.latitude}, "lon": {location.longitude}}

print(stationPos)
