"""
--* coding: utf-8 *--
@Author:Eric Ma
@Year: 2022
@python version: python 3.8
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches


# read the csv file
data = pd.read_csv('daniel.csv')

# drop out the columns called 'thermistor' and 'time' and "first column"
data = data.iloc[:, 1:69].drop(columns=['time', 'thermistor'])

# generate a DataFrame called 'coordinates' which will present the coordinates of location
x = data.iloc[:, 64].values
y = data.iloc[:, 65].values
d = {'x': x, 'y': y}
coordinates = pd.DataFrame(d)

"""
* plot the coordinates included "boundary"
* spilt the coordinates by "in/out of coverage"
* "i" means "in coverage"
* "o" means "out of coverage"
"""

# splitting
# i = coordinates[(coordinates.x <= -1.44) | (coordinates.x >= 1.44) | (coordinates.y >= 3.94) | (coordinates.y <= 1.1)]
# o = coordinates[(coordinates.x > -1.44) & (coordinates.x < 1.44) & (coordinates.y < 3.94) & (coordinates.y > 1.1)]


i = coordinates[(coordinates.x <= -0.40) | (coordinates.x >= 0.40) | (coordinates.y >= 2.9) | (coordinates.y <= 2.1)]
o = coordinates[(coordinates.x > -0.40) & (coordinates.x < 0.40) & (coordinates.y < 2.9) & (coordinates.y > 2.1)]

# plot the chart

fig1, ax1 = plt.subplots()
ax1.scatter(i.x, i.y, color="black")
ax1.scatter(o.x, o.y, color="green")
ax1.set_ylim(ymin=-1)
ax1.set_xlim(xmin=-4)
ax1.add_patch(
    patches.Rectangle(
        (-1.44, 1.1),  # Coordinate(x ,y)
        2.88,  # width
        2.88,  # height
        fill=None,  # fill color
        color="orange",  # line color
    )
)

ax1.add_patch(patches.Rectangle(
    (-0.4, 2.1),  # Coordinate(x ,y)
    0.8,  # width
    0.8,  # height
    fill=None,  # fill color
    color="red",  # line color
))

plt.show()
