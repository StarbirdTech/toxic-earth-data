
from geopy.geocoders import Nominatim
import pandas as pd
import numpy as np


data = pd.read_csv('co2/input-data/Co2Data.csv').to_numpy()
geolocator = Nominatim(user_agent='geopy test')

countries = np.unique(data[:, 0]).tolist()

countryPos = {}
for country in countries:
    location = geolocator.geocode(country)
    try:
        print((location.latitude, location.longitude))
    except:
        if country == "French Equatorial Africa":
            countryPos[country] = {"lat": {9}, "lon": {19}}
        if country == "French West Africa":
            countryPos[country] = {"lat": {16}, "lon": {0}}
        if country == "St. Kitts-Nevis-Anguilla":
            countryPos[country] = {"lat": {17.751983}, "lon": {-62.955379}}
    else:
        countryPos[country] = {
            "lat": {location.latitude}, "lon": {location.longitude}}

print(countryPos)
