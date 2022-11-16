import pandas as pd
import numpy as np
import os

target = "aqi"

allData = np.array([np.array([0, 0, 0])])

for file in os.listdir(f'{target}/output-data/'):
    allData = np.concatenate((allData, pd.read_csv(
        f'{target}/output-data/{file}').to_numpy()), axis=0) # convert to dateTime here

allData = allData[1:]

for year in range(2014, 2022):

    #? for this year part: feed year plus a stored list of cutoff points for each quarter into a np or pandas between date
    #? loop over the above for each element of the cutoff points array and replace location and save

    yearData = allData[np.where(toDateTimeObject(allData[:, 1]).getYear() == year)]

    q1 = np.averageDupe(yearData[np.where(toDateTimeObject(yearData[:, 1]) is between("start date", "end date"))], yearData[:, 1])
    q2 = np.averageDupe(yearData[np.where(toDateTimeObject(yearData[:, 1]) is between("start date", "end date"))], yearData[:, 1])
    q3 = np.averageDupe(yearData[np.where(toDateTimeObject(yearData[:, 1]) is between("start date", "end date"))], yearData[:, 1])
    q4 = np.averageDupe(yearData[np.where(toDateTimeObject(yearData[:, 1]) is between("start date", "end date"))], yearData[:, 1])

    #! SAVE TO FOLDER OTHER THAN OUTPUT-DATA
    for i, info in enumerate(q1):
        yearData[i, 1] = geocodedData[info[i,0]["lon"]]
        yearData[i, 0] = geocodedData[info[i, 0]["lat"]]
    pd.DataFrame(q1).to_csv(
        f'co2/output-data/{year}-q1.csv', index=False, header=["lat", "lon", "aqi"])

    for i, info in enumerate(q2):
        yearData[i, 1] = geocodedData[info[i, 0]["lon"]]
        yearData[i, 0] = geocodedData[info[i, 0]["lat"]]
    pd.DataFrame(q2).to_csv(
        f'co2/output-data/{year}-q2.csv', index=False, header=["lat", "lon", "aqi"])

    for i, info in enumerate(q3):
        yearData[i, 1] = geocodedData[info[i, 0]["lon"]]
        yearData[i, 0] = geocodedData[info[i, 0]["lat"]]
    pd.DataFrame(q3).to_csv(
        f'co2/output-data/{year}-q3.csv', index=False, header=["lat", "lon", "aqi"])

    for i, info in enumerate(q4):
        yearData[i, 1] = geocodedData[info[i, 0]["lon"]]
        yearData[i, 0] = geocodedData[info[i, 0]["lat"]]
    pd.DataFrame(q4).to_csv(
        f'co2/output-data/{year}-q4.csv', index=False, header=["lat", "lon", "aqi"])
