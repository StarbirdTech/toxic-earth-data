from importlib.machinery import SourceFileLoader
import pandas as pd
import numpy as np
import json

geocode = SourceFileLoader('geocode', 'geocode.py').load_module()

targetFolder = 'co2'

data = pd.read_csv(f'{targetFolder}/input-data/Co2Data.csv').dropna().to_numpy()

if input('Check geocode data?') == 'y':
    with open(f'{targetFolder}/geocode/inputData.json', "w") as outfile:
        json.dump(np.unique(data[:, 0]).tolist(), outfile)

    geocode.geocode(targetFolder, warnSkip=True)

geocodeData = json.load(open(f'{targetFolder}/geocode/outputData.json'))

for year in range(1750, 2021):
    yearData = data[np.where(data[:, 1] == year)]
    for i, info in enumerate(yearData):
        yearData[i, 1] = geocodeData[info[0]]['lon']
        yearData[i, 0] = geocodeData[info[0]]['lat']
    pd.DataFrame(yearData).to_csv(
        f'co2/output-data/{year}.csv', index=False, header=["lat", "lon", "co2"])

print('✔  All Data Saved')
