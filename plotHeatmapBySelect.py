import matplotlib.pyplot as plt
import pandas as pd
import tkinter as tk
from tkinter import simpledialog
import seaborn as sns
import matplotlib.patches as patches


data = pd.read_csv('daniel.csv')
data = data.iloc[:, 1:69].drop(columns=['time', 'thermistor'])

# pick up the specific location by entering
inputRow = tk.Tk()
inputRow.withdraw()
row_INP = simpledialog.askstring(title="plot", prompt="please enter the row")
inputRow_int = int(row_INP)
location_X = data.iloc[inputRow_int, 64]
location_Y = data.iloc[inputRow_int, 65]

fig2, axi2 = plt.subplots()
axi2.scatter(location_X, location_Y, color="red")
axi2.set_ylim(ymin=-1)
axi2.set_ylim(ymax=5)
axi2.set_xlim(xmin=-4)
axi2.set_xlim(xmax=3)
axi2.add_patch(
    patches.Rectangle(
        (-1.44, 1.1),  # Coordinate(x ,y)
        2.88,  # width
        2.88,  # height
        fill=None,  # fill color
        color="orange",  # line color
    )
)

axi2.add_patch(patches.Rectangle(
    (-0.20, 1.64),  # Coordinate(x ,y)
    0.4,  # width
    0.4,  # height
    fill=None,  # fill color
    color="red",  # line color
))

title = plt.title("coordinates: " + "(" + str(location_X) + ", " + str(location_Y) + ")")
plt.setp(title, color='r')
# ************************************************************************************************
"""
Here is a part that will be used to plot the heat map

note:
    *   1468 - center      *
    *   5487 - topRight    *
    *   1099 - lowerRight  *
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
    Re_df = Re_df[::-1, ::-1]
    df = Re_df
    return df


heatmap = reshape(point)

# plotting the heatmap
fig3, axi3 = plt.subplots()
sns.heatmap(heatmap, annot=True, linewidths=0.5, cmap='hot_r', fmt='2g', vmax=0.5, vmin=3.8)
title = plt.title("coordinates: " + "(" + str(location_X) + ", " + str(location_Y) + ")")
plt.setp(title, color='r')

plt.show()
