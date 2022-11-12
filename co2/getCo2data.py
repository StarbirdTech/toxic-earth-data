from geopy.geocoders import Nominatim
import pandas as pd
import numpy as np

data = pd.read_csv('Co2Data.csv').to_numpy()
geolocator = Nominatim(user_agent='geopy test')

countries = np.unique(data[:, 0])
sorted = data[data[:, 1].argsort()]
print(sorted)

# for year in range(1750, 2021):
#     yearData = data[np.where(data[:, 1] == year)]

#     pd.DataFrame(yearData).to_csv(f'output-data/{year}.csv', index=False)

countryPos = {}
for country in countries:
    location = geolocator.geocode(country)
    try:
        print((location.latitude, location.longitude))
    except:
        if country == "French Equatorial Africa":
            countryPos[country] = {"lat": {1}, "lon": {1}}
        if country == "French West Africa":
            countryPos[country] = {"lat": {1}, "lon": {1}}
        if country == "St. Kitts-Nevis-Anguilla":
            countryPos[country] = {"lat": {1}, "lon": {1}}
    else:
        countryPos[country] = {
            "lat": {location.latitude}, "lon": {location.longitude}}

fakeStuff = {
    "St. Kitts-Nevis-Anguilla": {"lat": 34, "lon": 45},
    "French West Africa": {"lat": 34, "lon": 45},
    "French Equatorial Africa": {"lat": 34, "lon": 45}
}

fakeStuff["newentry"] = 5
print(fakeStuff)
