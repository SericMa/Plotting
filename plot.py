"""
--* coding: utf-8 *--
@Author:Eric Ma
@Year: 2022
@python version: python 3.8
"""
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

# splitting
i = coordinates[(coordinates.x <= -1.45) | (coordinates.x >= 1.45) | (coordinates.y >= 3.98) | (coordinates.y <= 1.1)]
o = coordinates[(coordinates.x > -1.45) & (coordinates.x < 1.45) & (coordinates.y < 3.98) & (coordinates.y > 1.1)]

# plot the chart
"""
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
"""

# pick up the specific location by entering
inputRow = tk.Tk()
inputRow.withdraw()
row_INP = simpledialog.askstring(title="plot", prompt="please enter the row")
# inputRow = input('input row wanted: ')
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
plt.show()


