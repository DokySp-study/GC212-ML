import numpy as np



t = np.array([0, 1]).reshape(1,2)

p = np.array([0.9, 0.1, 0.2, 0.8]).reshape(2,2)

print(t)
print(p)


tt = np.array([0.6, 0.4]).reshape(1,2)

print(tt)
print(tt@p@p@p)