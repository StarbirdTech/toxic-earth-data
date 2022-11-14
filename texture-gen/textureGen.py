from PIL import Image, ImageDraw
import pandas as pd
import numpy as np
import math
import os


def myMap(input, start1, stop1, start2, stop2):
    return ((input-start1)/(stop1-start1))*(stop2-start2)+start2


def clamp(num, min_value, max_value):
    return max(min(num, max_value), min_value)


target = "co2"

for file in os.listdir(f'{target}/output-data/'):
    #print(file.split(".", 1)[0])
    data = pd.read_csv(f'{target}/output-data/{file}').to_numpy()

    im = Image.new("L", (800, 400))
    draw = ImageDraw.Draw(im)

    dataMin = np.min(data, axis=0)[2]
    dataMax = np.max(data, axis=0)[2]

    for year in data:
        #light = (year[2]**2/max(year[2], 0)+0)/dataMax*255
        # print(light)
        # print(np.array((data-min(data))**2))
        # print(year[2])
        #  print(np.array(((data)**2)/max((data-min(data)))) +
        #      min(data)[i]/max(data)*255)
        # print(myMap(np.array(((data-min(data))**2) /
        #      max((data-min(data))))+min(data)[i]))

        draw.point((myMap(year[1], -180, 180, 0, 800), myMap(year[0],
                                                             90, -90, 0, 400)), fill=int(myMap(year[2], 0, 500, 0, 255)))

    im.save(f'{target}/output-textures/{file.split(".", 1)[0]}.png')

    # int(myMap(data[i][2], 0, data[:, 2].max(), 0, 255))
    # expData = np.array(((data-min(data))**2)/max((data-min(data))))+min(data)
