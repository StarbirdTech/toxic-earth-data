from PIL import Image, ImageDraw
import pandas as pd
import numpy as np
import math
import os
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent='geopy test')


def myMap(input, start1, stop1, start2, stop2):
    return ((input-start1)/(stop1-start1))*(stop2-start2)+start2


def clamp(num, min_value, max_value):
    return max(min(num, max_value), min_value)


def scaleLog(a, mini, maxi, factor):
    return np.round((a-mini)*np.power(a/maxi, 1/factor)+mini)


target = "co2"

allData = np.array([np.array([0, 0, 0])])

for file in os.listdir(f'{target}/final-output-data/'):
    allData = np.concatenate((allData, pd.read_csv(
        f'{target}/final-output-data/{file}').to_numpy()), axis=0)

allData = allData[1:]

print(allData)
co2data = allData[:, 2]
# print(co2data)
expCo2data = np.array((co2data-np.min(co2data))**2) / \
    (np.max(co2data)+np.min(co2data))
# print(expCo2data)

dataMin = np.min(co2data)
dataMax = np.max(co2data)

rowCount = 0

print(os.listdir(f'{target}/final-output-data/'))

for file in os.listdir(f'{target}/final-output-data/'):
    data = pd.read_csv(f'{target}/final-output-data/{file}').to_numpy()
    #worstestbreathus = data[np.argmax(data[:, 2])]
    #print(worstestbreathus)
    #reverseGeocodedLocation = geolocator.reverse(
    #    (worstestbreathus[0], worstestbreathus[1]), addressdetails=False)
    #reverseGeocodedLocation = reverseGeocodedLocation.split(",")
    #print((reverseGeocodedLocation.city, reverseGeocodedLocation.country))

    im = Image.new("L", (800, 400))
    draw = ImageDraw.Draw(im)
    # print(os.listdir(
    # f'{target}/output-data/').index(file))
#
    #rowCount += len(data)-1
    #print(len(data))
    for i in range(len(data)):
        #         #light = (year[2]**2/max(year[2], 0)+0)/dataMax*255
        #         # print(light)
        #    #         # print(np.array((data-min(data))**2))
        #    #         # print(year[2])
        #    #         #  print(np.array(((data)**2)/max((data-min(data)))) +
        #    #         #      min(data)[i]/max(data)*255)
        #    # print(myMap(np.array(((data-min(data))**2) /
        #    #                     max((data-min(data))))+min(data)[i]))
        x = myMap(data[i, 1], -180, 180, 0, 800)
        y = myMap(data[i, 0], 90, -90, 0, 400)
        fill = myMap(scaleLog(data[i, 2], dataMin, dataMax, 10),dataMin,dataMax,10,255)
        print(fill)
        draw.point((x, y), int(fill))

    #    # draw.point((myMap(data[i][1], -180, 180, 0, 800), myMap(data[i][0], 90, -90,
    #    # 0, 400)), fill=int(myMap((data[i][2]-np.min(co2data))**2) / (np.max(co2data)+np.min(co2data)), 0, np.max(co2data), 0, 255))
    # im.show()

    quarters = {
        "q1": "Winter",
        "q2": "Spring",
        "q3": "Summer",
        "q4": "Fall",
    }

    #worstestbreathus = data[np.argmax(data[:, 2])]

    im.save(f'{target}/final-output-textures/aqi-{file.split(".", 1)[0]}.png')
        #f'{target}/output-textures/aqi-{file.split(".", 1)[0].split("-")[0]}-{quarters[file.split(".", 1)[0].split("-")[1]]}-.png')

    # int(myMap(data[i][2], 0, data[:, 2].max(), 0, 255))
    # expData = np.array(((data-min(data))**2)/max((data-min(data))))+min(data)
