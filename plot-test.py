

import matplotlib.pyplot as plt
import numpy as np
import math


def myMap(input, start1, stop1, start2, stop2):
    return ((input-start1)/(stop1-start1))*(stop2-start2)+start2


def myNewMap(input, start1, stop1, start2, stop2):
  # math.log10((input+math.sqrt((input*input))+4)/2)
    return math.log10(input/2)


def clamp(num, min_value, max_value):
    return max(min(num, max_value), min_value)


x = np.linspace(0, 1000, 100)
y = np.ones(100)

# int(myMap(data[i][2], 0, data[:, 2].max(), 0, 255))

for num in range(len(x)):
    y[num] = clamp(math.log(x[num]/1000+1), 0, 1)

plt.plot(x, y)

plt.show()
