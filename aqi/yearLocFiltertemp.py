from importlib.machinery import SourceFileLoader
import pandas as pd
import numpy as np
import os
import json

geocode = SourceFileLoader('geocode', 'geocode.py').load_module()

targetFolder = 'aqi'

allData = np.array([np.array([0, 0, 0])])

for file in os.listdir(f'{targetFolder}/output-data/'):
    try:
        allData = np.concatenate((allData, pd.read_csv(
            f'{targetFolder}/output-data/{file}').to_numpy()), axis=0)
    except:
        print(f'no data in {file}')

allData = allData[1:]

print(allData)

if input('Check geocode data?') == 'y':
    with open(f'{targetFolder}/geocode/inputData.json', "w") as outfile:
        json.dump(np.unique(allData[:, 0]).tolist(), outfile)

    geocode.geocode(targetFolder, warnSkip=True)

geocodeData = json.load(open(f'{targetFolder}/geocode/outputData.json'))

df = pd.DataFrame(allData, columns=['location', 'date', 'aqi'])

dates = [['01-01', '03-31'], ['04-01', '06-31'],
         ['7-01', '09-30'], ['10-01', '12-31']]

noDataCount = 0

for year in range(2014, 2022):
    yearData = allData[np.where(
        pd.DatetimeIndex(allData[:, 1]).year == year)]
    quarterCount = 1
    for dateRange in dates:
        mask = (df['date'] > str(year) + '-'+dateRange[0]
                ) & (df['date'] <= str(year)+'-'+dateRange[1])
        rangedData = df.loc[mask]
        # print(f'{year}, from {dateRange[0]} to {dateRange[1]}: Quarter {quarterCount}')
        # print(rangedData)
        # print('__________')
        rangedData = rangedData.to_numpy()

        for i, info in enumerate(rangedData):
            try:
                locationData = geocodeData[info[0]]
            except:
                noDataCount += 1
            else:
                newRow = np.array(
                    [locationData['lat'], locationData['lon'], rangedData[i, 2]])
                try:
                    finalOutput = np.row_stack((finalOutput, newRow))
                except:
                    finalOutput = newRow
                    print('overwrite output ❌')

        # print(pd.DataFrame(finalOutput))

        if len(finalOutput[0]) != 0:
            pd.DataFrame(finalOutput).to_csv(
                f'aqi/final-output-data/{year}-q{quarterCount}.csv', index=False, header=['lat', 'lon', 'aqi'])

        quarterCount += 1

    # print(rangedData)

# for year in range(2014, 2022):
#
#    #? for this year part: feed year plus a stored list of cutoff points for each quarter into a np or pandas between date
#    #? loop over the above for each element of the cutoff points array and replace location and save
#
#    yearData = allData[np.where(toDateTimeObject(allData[:, 1]).getYear() == year)]
#
#    q1 = np.averageDupe(yearData[np.where(toDateTimeObject(yearData[:, 1]) is between("start date", "end date"))], yearData[:, 1])
#    q2 = np.averageDupe(yearData[np.where(toDateTimeObject(yearData[:, 1]) is between("start date", "end date"))], yearData[:, 1])
#    q3 = np.averageDupe(yearData[np.where(toDateTimeObject(yearData[:, 1]) is between("start date", "end date"))], yearData[:, 1])
#    q4 = np.averageDupe(yearData[np.where(toDateTimeObject(yearData[:, 1]) is between("start date", "end date"))], yearData[:, 1])
#
#    #! SAVE TO FOLDER OTHER THAN OUTPUT-DATA
#    for i, info in enumerate(q1):
#        yearData[i, 1] = geocodedData[info[i,0]["lon"]]
#        yearData[i, 0] = geocodedData[info[i, 0]["lat"]]
#    pd.DataFrame(q1).to_csv(
#        f'co2/output-data/{year}-q1.csv', index=False, header=["lat", "lon", "aqi"])
#
#    for i, info in enumerate(q2):
#        yearData[i, 1] = geocodedData[info[i, 0]["lon"]]
#        yearData[i, 0] = geocodedData[info[i, 0]["lat"]]
#    pd.DataFrame(q2).to_csv(
#        f'co2/output-data/{year}-q2.csv', index=False, header=["lat", "lon", "aqi"])
#
#    for i, info in enumerate(q3):
#        yearData[i, 1] = geocodedData[info[i, 0]["lon"]]
#        yearData[i, 0] = geocodedData[info[i, 0]["lat"]]
#    pd.DataFrame(q3).to_csv(
#        f'co2/output-data/{year}-q3.csv', index=False, header=["lat", "lon", "aqi"])
#
#    for i, info in enumerate(q4):
#        yearData[i, 1] = geocodedData[info[i, 0]["lon"]]
#        yearData[i, 0] = geocodedData[info[i, 0]["lat"]]
#    pd.DataFrame(q4).to_csv(
#        f'co2/output-data/{year}-q4.csv', index=False, header=["lat", "lon", "aqi"])
#
