from PIL import Image, ImageDraw
import pandas as pd
import numpy as np
import math
import os
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent='geopy test')


def myMap(input, start1, stop1, start2, stop2):
    return ((input-start1)/(stop1-start1))*(stop2-start2)+start2


target = 'aqi'

for file in os.listdir(f'{target}/ranking/'):
    data = pd.read_csv(f'{target}/ranking/{file}').to_numpy()

    im = Image.new("L", (800, 400))
    draw = ImageDraw.Draw(im)
    
    for i in range(len(data)):
        x = myMap(data[i, 1], -180, 180, 0, 800)
        y = myMap(data[i, 0], 90, -90, 0, 400)
        fill = data[i,2]

        draw.point((x, y), int(255))

    quarters = {
        "q1": "Winter",
        "q2": "Spring",
        "q3": "Summer",
        "q4": "Fall",
    }

    im.save(f'{target}/final-output-textures/aqi-{file.split(".", 1)[0]}.png')
