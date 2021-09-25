import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt

# X1 = np.array([1.01, 1.00, 1.01, 1.04, 1.09])

X = np.array([-2, -1, 0, 1, 2])
target = np.array([1, 1, 0, 1, 1])

center1 = np.array([-3, 0])
center2 = np.array([2, 0])
gamma = 0.01

ansTrueX = []
ansFalseX = []
ansTrueY = []
ansFalseY = []

for i in range(0, len(X)):
    x = np.array([X[i], 0])
    res = np.exp( - gamma * np.power((x - center1), 2) )
    if target[i] == 1:
        ansTrueX.append(res[0])
    else: 
        ansFalseX.append(res[0])

for i in range(0, len(X)):
    x = np.array([X[i], 0])
    res = np.exp( - gamma * np.power((x - center2), 2) )
    if target[i] == 1:
        ansTrueY.append(res[0])
    else: 
        ansFalseY.append(res[0])

# plt.plot(X, [0,0,0,0,0], "bo")
# plt.plot(0, 0, "ro")
# plt.xlabel("Existing feature: X")
# plt.show()


print(ansTrueX)
print(ansFalseX)
print("")
print(ansTrueY)
print(ansFalseY)



plt.plot(ansTrueX, ansTrueY, "bo")
plt.plot(ansFalseX, ansFalseY, "ro")
plt.title("RBF (γ = 0.1)")
plt.xlabel("X_new1, using (-1,0) as center")
plt.ylabel("X_new2, using (2,0) as center")

plt.show()




