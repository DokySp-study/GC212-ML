
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


r = 25 #26



df = pd.DataFrame({
    "x": [30,   90, 160, 249, 294,   8,  70, 114,  24,  94, 275, 233, 76, 114, 156, 116, 34, 67, 21, 87,    189, 180, 209, 220, 242, 240, 266, 273, 273, 286, 283, 306],
    "y": [155, 155, 155, 155, 155, 137, 124, 118, 104, 106, 104, 100, 87,  94,  91,  75, 62, 50, 31, 19,     50,   6,  19,  37,  25,   6,  31,   6,  44,  56,  37,  56],
})

# ggggg
dfg = pd.DataFrame({
    "x": [],
    "y": [],
})
dfgg = pd.DataFrame({
    "x": [306,283,286,273,242,266,220,209,240,273,189,180],
    "y": [56,  37, 56, 44,25,  31, 37, 19,  6,  6,50 ,6],
})
 
# Outlier
dfy = pd.DataFrame({
    "x": [156, 30,  8, 24,34,21,67,87, 90,160,249,294,233,275],
    "y": [91 ,155,137,104,62,31,50,19,155,155,155,155,100,104]
})

# bbbbbbb
dfb = pd.DataFrame({
    "x": [ ],
    "y": [],
})

dfbb = pd.DataFrame({
    "x": [],
    "y": [],
})


# rrrrrr
dfr = pd.DataFrame({
    "x": [],
    "y": [],
})

dfrr = pd.DataFrame({
    "x": [114,94, 114,70 ,76,116],
    "y": [118,106,94 ,124,87,75 ],
})





# pppppp
dfp = pd.DataFrame({
    "x": [],
    "y": [],
})

dfpp = pd.DataFrame({
    "x": [],
    "y": [],
})




# plt.figure(figsize=(9, 7))
# plt.plot(df['x'], df['y'], "ko", markersize=15)

# plt.plot(dfr['x'], dfr['y'], "ro", markersize=15)
# plt.plot(dfrr['x'], dfrr['y'], "o", markersize=15, markeredgewidth=2, markeredgecolor=[1,0,0],  markerfacecolor=[1,0.5,0.5])


# plt.plot(dfg['x'], dfg['y'], "o", markersize=15, markeredgecolor=[0,1,0],  markerfacecolor=[0,1,0])
# plt.plot(dfgg['x'], dfgg['y'], "o", markersize=15, markeredgewidth=2, markeredgecolor=[0,1,0],  markerfacecolor=[0.5,1,0.5])

# plt.plot(dfb['x'], dfb['y'], "o", markersize=15, markeredgecolor=[0,0,1],  markerfacecolor=[0,0,1])
# plt.plot(dfbb['x'], dfbb['y'], "o", markersize=15, markeredgewidth=2, markeredgecolor=[0,0,1],  markerfacecolor=[0.5,0.5,1])

# plt.plot(dfp['x'], dfp['y'], "o", markersize=15, markeredgecolor=[0.7,0,1],  markerfacecolor=[0.7,0,1])
# plt.plot(dfpp['x'], dfpp['y'], "o", markersize=15, markeredgewidth=2, markeredgecolor=[0.7,0,1],  markerfacecolor=[0.8,0.5,1])

# plt.plot(dfy['x'], dfy['y'], "o", markersize=15,  markeredgecolor=[1,0.7,0],  markerfacecolor=[1,0.7,0])

# ax = plt.gca()
# ax.axes.xaxis.set_visible(True)
# ax.axes.yaxis.set_visible(True)

# plt.show()


plt.figure(figsize=(9, 6))
# plt.plot(df['x'], df['y'], "ko", markersize=15)

plt.plot(dfr['x'], dfr['y'], "ro", markersize=15)
plt.plot(dfrr['x'], dfrr['y'], "o", markersize=15, markeredgewidth=2, markeredgecolor=[1,0,0],  markerfacecolor=[1,0.5,0.5])


plt.plot(dfg['x'], dfg['y'], "o", markersize=15, markeredgecolor=[0,1,0],  markerfacecolor=[0,1,0])
plt.plot(dfgg['x'], dfgg['y'], "o", markersize=15, markeredgewidth=2, markeredgecolor=[0,1,0],  markerfacecolor=[0.7,1,0.7])

plt.plot(dfb['x'], dfb['y'], "o", markersize=15, markeredgecolor=[0,0,1],  markerfacecolor=[0,0,1])
plt.plot(dfbb['x'], dfbb['y'], "o", markersize=15, markeredgewidth=2, markeredgecolor=[0,0,1],  markerfacecolor=[0.5,0.5,1])

plt.plot(dfp['x'], dfp['y'], "o", markersize=15, markeredgecolor=[0.7,0,1],  markerfacecolor=[0.7,0,1])
plt.plot(dfpp['x'], dfpp['y'], "o", markersize=15, markeredgewidth=2, markeredgecolor=[0.7,0,1],  markerfacecolor=[0.8,0.5,1])

plt.plot(dfy['x'], dfy['y'], "o", markersize=10,  markeredgecolor=[1,0.7,0],  markerfacecolor=[1,0.7,0])

ax = plt.gca()
ax.axes.xaxis.set_visible(False)
ax.axes.yaxis.set_visible(False)

plt.show()
