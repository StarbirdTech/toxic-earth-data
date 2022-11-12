from PIL import Image, ImageDraw
import pandas as pd
import numpy as np
import math


def myMap(input, start1, stop1, start2, stop2):
    return ((input-start1)/(stop1-start1))*(stop2-start2)+start2


def clamp(num, min_value, max_value):
    return max(min(num, max_value), min_value)


target = "co2"

data = pd.read_csv(f'{target}/output-data/2020.csv').to_numpy()
data[np.isnan(data)] = 0

print(data[:, 2].max())

im = Image.new("L", (800, 400))
draw = ImageDraw.Draw(im)

for i in range(len(data)):
    try:
        draw.point((myMap(data[i][1], -180, 180, 0, 800), myMap(data[i][0], 90, -90,
                                                                0, 400)), fill=int(myMap(clamp(math.log(data[i][2]/1000+1), 0, 1), 0, .7, 0, 255)))
    except:
        print(f'Invalid data at {i}')

im.save(f'{target}/output-textures/2020-log.png')

# int(myMap(data[i][2], 0, data[:, 2].max(), 0, 255))
