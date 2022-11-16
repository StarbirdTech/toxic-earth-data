from geopy.geocoders import Nominatim
import json

def geocode(targetFolder, warnSkip=False):
    geolocator = Nominatim(user_agent='geopy test')

    inputData = json.load(open(f'{targetFolder}/geocode/inputData.json'))

    try:
        outputDataLoaded = json.load(
            open(f'{targetFolder}/geocode/outputData.json'))
    except:
        print('⚠️  outputData file not found: No data with be auto-loaded')

    try:
        manualData = json.load(open(f'{targetFolder}/geocode/outputManualData.json'))
    except:
        manualData = {}
        print('⚠️  outputManual file not found: No manual data with be auto-loaded')

    stationPosManualToSet = []
    outputData = {}

    for location in inputData:
        try:
            outputData[location] = outputDataLoaded[location]
            print('loaded from output')
        except:
            try:
                geocodedLocation = geolocator.geocode(location)
                outputData[location] = {
                    "lat": geocodedLocation.latitude, "lon": geocodedLocation.longitude}
                print('loaded from api')
            except:
                try:
                    outputData[location] = manualData[location]
                except:
                    stationPosManualToSet.append(location)
                    print(f'⚠️  No data found for {location}')
                else:
                    print(f'🎉  Manual data auto-loaded for {location}')
    print('data load done')
    #for location in stationPosManualToSet:
    #    while True:
    #        userInput = input(
    #            f'Enter lat & lon for {location} separated by a comma\nExample: 19.8,20.95\n')
    #        result = userInput.split(',')
    #        try:
    #            lat = float(result[0])
    #            lon = float(result[1])
    #        except:
    #            print(f'{userInput} is not valid, please only enter numbers')

    #        if input(f'Location Name: {location}\nLat: {result[0]}\nLon: {result[1]}\nPress "y" to confirm:\n') == 'y':
    #            outputData[location] = manualData[location] = {"lat": lat, "lon": lon}
    #            print(f'✔  {location} data set')
    #            break
    #        else:
    #            if warnSkip:
    #                print('⚠ Skipping items may cause unexpected behavior')
    #            if input("s to skip") == 's':
    #                break

    print('🥳  Data Ready  🥳')

    #if warnSkip:
    #    print('⚠ Not saving data may cause unexpected behavior')
#
    #if input('Would you like to save data?\n') == 'y':
    with open(f'{targetFolder}/geocode/outputData.json', "w") as outfile:
        json.dump(outputData, outfile)
        #print('✔  Data Saved')

    #if input('Would you like to save manually filled data?\n') == 'y':
    with open(f'{targetFolder}/geocode/outputManualData.json', "w") as outfile:
        json.dump(manualData, outfile)
        #print('✔  Manual Data Saved')
