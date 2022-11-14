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
    data = pd.read_csv(f'{target}/output-data/{file}').to_numpy()
    data[data == ''] = 0

    im = Image.new("L", (800, 400))
    draw = ImageDraw.Draw(im)

    for i in range(len(data)):
        try:
            draw.point((myMap(data[i][1], -180, 180, 0, 800), myMap(data[i][0], 90, -90,
                                                                    0, 400)), fill=int(myMap(clamp(math.log(data[i][2]/1000+1), 0, 1), 0, .7, 0, 255)))
        except:
            print(f'Invalid data at {i}')

    im.save(f'{target}/output-textures/{file.split()}.png')

    int(myMap(data[i][2], 0, data[:, 2].max(), 0, 255))
