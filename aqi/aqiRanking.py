from geopy.geocoders import Nominatim

import pandas as pd
import numpy as np
import os

geolocator = Nominatim(user_agent='geopy test')

for file in os.listdir('aqi/final-output-data'):
  data = pd.read_csv(f'aqi/final-output-data/2014-q1.csv').to_numpy()
  data = np.flip(data[data[:,2].argsort()], axis=0)

#outputData = []
#for row in data:
#  location = geolocator.reverse((row[0], row[1]), exactly_one=True, language='en')
#  
#  city = location.raw.get('address').get('city')
#  country = location.raw.get('address').get('country')
#  print(f'{city}, {country}')
  #print(len(data))
  #print(np.linspace(255, 0, num=len(data)))
  #data[:2] = np.linspace(255, 0, num=len(data))

  finalData = np.column_stack((data[:, 0], data[:, 1], np.linspace(255, 100, num=len(data))))

  pd.DataFrame(finalData).to_csv(
      f'aqi/ranking/{file}', index=False, header=["lat", "lon", "aqi"])
