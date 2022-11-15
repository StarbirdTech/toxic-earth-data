
#from geopy.geocoders import Nominatim
import pandas as pd
import numpy as np
import json

### Station Headers ###
#   0:  stationName
#   1:  stationID

geolocator = {"Town": {"latitude": 5, "longitude": 5}, "Short": {"latitude": 10, "longitude": 10},
              "Monkey": {"latitude": 7, "longitude": 7}}  # Nominatim(user_agent='geopy test')

stations = json.load('aqi/stations.json')

try:
    stationPosManual = json.load('aqi/stationPosManual.json')
except:
    stationPosManual = {}
    print('🟡   stationPosManual file not found: No manual data with be auto-loaded')

print(stations)
stationPosManualToSet = []
stationPos = {}

for station in stations:
    # location = geolocator.geocode(station) #uncomment
    try:
        location = geolocator[station]  # remove
        print((location.latitude, location.longitude))
    except:
            try:
                stationPos[station] = {
                    "lat": stationPosManual[station].lat, "lon": stationPosManual[station].lon}
            except:
                stationPosManualToSet.append(station)
                print(f'⚠️  No data found for {station}')
            else:
                print(f'🎉  Manual data auto-loaded for {station}')
    else:
        stationPos[station] = {
            "lat": location.latitude, "lon": location.longitude}

print(stationPos)
