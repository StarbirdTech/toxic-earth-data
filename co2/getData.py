from countryPos import countryPos
import pandas as pd
import numpy as np


def getPos(loc, cord):
    return float(str(countryPos[loc][cord]).replace('{', '').replace('}', ''))


data = pd.read_csv('co2/input-data/Co2Data.csv').dropna().to_numpy()

for year in range(1750, 2021):
    yearData = data[np.where(data[:, 1] == year)]
    for i, info in enumerate(yearData):
        yearData[i, 1] = getPos(info[0], "lon")
        yearData[i, 0] = getPos(info[0], "lat")
    pd.DataFrame(yearData).to_csv(
        f'co2/output-data/{year}.csv', index=False, header=["lat", "lon", "co2"])
