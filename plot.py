"""
--* coding: utf-8 *--
@Author:Eric Ma
@Year: 2022
@python version: python 3.8
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import tkinter as tk
from tkinter import simpledialog
import seaborn as sns

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

# # splitting
# i = coordinates[(coordinates.x <= -1.44) | (coordinates.x >= 1.44) | (coordinates.y >= 3.94) | (coordinates.y <= 1.1)]
# o = coordinates[(coordinates.x > -1.44) & (coordinates.x < 1.44) & (coordinates.y < 3.94) & (coordinates.y > 1.1)]
#
# # plot the chart
#
# fig1, ax1 = plt.subplots()
# ax1.scatter(i.x, i.y, color="black")
# ax1.scatter(o.x, o.y, color="green")
# ax1.add_patch(
#     patches.Rectangle(
#         (-1.44, 1.1),  # Coordinate(x ,y)
#         2.88,  # width
#         2.88,  # height
#         fill=None,  # fill color
#         color="orange",  # line color
#     )
# )


# pick up the specific location by entering
inputRow = tk.Tk()
inputRow.withdraw()
row_INP = simpledialog.askstring(title="plot", prompt="please enter the row")
inputRow_int = int(row_INP)
location_X = data.iloc[inputRow_int, 64]
location_Y = data.iloc[inputRow_int, 65]

fig2, axi2 = plt.subplots()
axi2.scatter(location_X, location_Y, color="red")
axi2.add_patch(
    patches.Rectangle(
        (-1.44, 1.1),  # Coordinate(x ,y)
        2.88,  # width
        2.88,  # height
        fill=None,  # fill color
        color="orange",  # line color
    )
)

title = plt.title("coordinates: " + "(" + str(location_X) + ", " + str(location_Y) + ")")
plt.setp(title, color='r')

# ************************************************************************************************
"""
Here is a part that will be used to plot the heat map

note:
    *   1468 - center coordinates       *
    *   5232 - topLeft coordinates      *
    *   5487 - topRight coordinates     *
    *   6595 - lowerLeft coordinates    *
    *   1099 - lowerRight coordinates   *
"""

# drop out the coordinates
thermal_data = data.drop(data.columns[[64, 65]], axis=1)

# simple background subtraction
background = data[(data['x'] < -1.47) | (data['x'] > 1.47) | (data['y'] < 1.05) |
                  (data['y'] > 4.02)]

background = background.drop(background.columns[[64, 65]], axis=1)

BK_SB = thermal_data - background.mean()

point = BK_SB.iloc[inputRow_int, :]


# reshape the DataFrame
def reshape(df):
    df = df.values
    Re_df = df.reshape(8, 8)
    Re_df = Re_df.astype(float)
    Re_df = np.rot90(Re_df, k=2)
    return Re_df


heatmap = reshape(point)

# plotting the heatmap
fig3, axi3 = plt.subplots()
sns.heatmap(heatmap, annot=True, linewidths=0.5, cmap='hot_r', fmt='2g')
title = plt.title("coordinates: " + "(" + str(location_X) + ", " + str(location_Y) + ")")
plt.setp(title, color='r')

plt.show()


# end
