
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt



df = pd.DataFrame({
    "x": [4, 14, 12, 24, 25, 36, 37, 49, 62],
    "y": [5, 10, 36, 14, 2,  18, 7,  13, 13],
})

dfrr = pd.DataFrame({
    "x": [36,24,37,49,14,25,62,4],
    "y": [18,14, 7,13,10,2 ,13,5],
})

dfr = pd.DataFrame({
    "x": [12],
    "y": [36],
})

dfy = pd.DataFrame({
    "x": [], # [24,37,49],
    "y": [] # [14, 7,13],
})

plt.figure(figsize=(9, 6))
plt.plot(df['x'], df['y'], "bo", markersize=15)
plt.plot(dfrr['x'], dfrr['y'], "o", markersize=15, markeredgewidth=2, markeredgecolor=[1,0,0],  markerfacecolor=[1,0.5,0.5])
plt.plot(dfr['x'], dfr['y'], "go", markersize=15, markeredgewidth=2, markeredgecolor=[1,1,0],  markerfacecolor=[1,1,0])
plt.plot(dfy['x'], dfy['y'], "o", markersize=15,  markeredgecolor=[1,1,0],  markerfacecolor=[1,1,0])

ax = plt.gca()
ax.axes.xaxis.set_visible(False)
ax.axes.yaxis.set_visible(False)

plt.show()