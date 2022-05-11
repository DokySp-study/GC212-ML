# Clustering with DBSCAN() and...
#  - housing_median_age
#  - total_rooms
#  - population

x=df['housing_median_age']
y=df['total_bedrooms']
z=df['population']
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.scatter(x, y, z, marker='o', s=5, c=labels)

ax.set_xlabel('housing_median_age', fontsize=10)
ax.set_ylabel('total_bedrooms', fontsize=10)
ax.set_zlabel('population', fontsize=10)
plt.show()
