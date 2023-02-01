import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = [1, 1, 2, 2]
y = [1, 2, 2, 1]
z = [0, 0, 0, 0]

ax.plot_trisurf(x, y, z)

x_rand = [random.uniform(1, 2) for i in range(10)]
y_rand = [random.uniform(1, 2) for i in range(10)]
z_rand = np.sqrt(5 - (np.power(x_rand, 2) + np.power(y_rand, 2)))

ax.scatter(x_rand, y_rand, z_rand, c='r', marker='o')
ax.plot_trisurf(x_rand, y_rand, z_rand)
plt.show()


# from mayavi import mlab
# import numpy as np
#
# mlab.figure(bgcolor=(1, 1, 1))
#
# x_val = [1, 1, 2, 2]
# y_val = [1, 2, 2, 1]
# z = [0, 0, 0, 0]
#
# triangles = [(0, 1, 2), (0, 2, 3)]
#
#
#
# x_rand = [np.random.uniform(1, 2) for i in range(10)]
# y_rand = [np.random.uniform(1, 2) for i in range(10)]
# z_rand = np.sqrt(5 - (np.power(x_rand, 2) + np.power(y_rand, 2)))
# triangles_rand = [(i, i+1, i+2) for i in range(0,len(x_rand)-2)]
#
# mlab.points3d(x_rand, y_rand, z_rand, color=(1, 0, 0), scale_factor=0.1)
#
# mlab.triangular_mesh(x_rand, y_rand, z_rand, triangles_rand, color=(1, 0, 0))
# mlab.show()