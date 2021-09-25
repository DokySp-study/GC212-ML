from matplotlib import pyplot as plt


plt.plot([0, 5.2], [0.59, 0.59, ], color="#FFBBBB")
plt.plot([0, 5.2], [0.85, 0.85, ], color="#BBBBFF")

plt.plot([0, 1, 2, 3, 4, 5], [0.1, 0.5, 0.55, 0.57, 0.58, 0.59], color="#FF7777")
plt.plot([0, 1, 2, 3, 4, 5], [0.9, 0.78, 0.83, 0.84, 0.85, 0.85], color="#7777FF")
plt.plot([0, 1, 2, 3, 4, 5], [0.1, 0.5, 0.55, 0.57, 0.58, 0.59], "ro")
plt.plot([0, 1, 2, 3, 4, 5], [0.9, 0.78, 0.83, 0.84, 0.85, 0.85], "bo")

plt.xlabel("EM Steps")
plt.ylabel("p, q value")

plt.show()