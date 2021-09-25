
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


df = pd.DataFrame({
    "x": [7, 2, 3, 8, 7, 4, 6, 7, 6, 3],
    "y": [6, 6, 8, 5, 4, 7, 2, 3, 4, 4],
})




# plt.plot(df.iloc[:,0], df.iloc[:,1], "bo")
# plt.plot([7, 3], [6, 8], "ro")
# plt.show()


min = 1000000000
minC1 = -1
minC2 = -1


for n in range(0, 10):
#     for m in range(n+1, 10):
    print(n)
    k1 = [df.iloc[n,0], df.iloc[n,1]]
    k2 = [df.iloc[4,0], df.iloc[4,1]]

    error = 0

    for i in range(0, 10):
        res1 = abs(df.iloc[i, 0] - k1[0]) + abs(df.iloc[i, 1] - k1[1]) 
        # print(res1, end=", ")
        res2 = abs(df.iloc[i, 0] - k2[0]) + abs(df.iloc[i, 1] - k2[1])
        # print(res2)

        if(res1 > res2):
            error += res2
        else:
            error += res1

    print("========")
    print(error)
    print("")

# if min > error : 
#     min = error
#     minC1 = n
#     minC2 = m




print("")
print(min)
print(minC1, end=", ")
print(minC2)