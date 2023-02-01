# # import numpy as np
# # import matplotlib.pyplot as plt
# #
# # # Create a grid of points
# # x_val, y_val = np.linspace(1, 10, 20), np.linspace(-1, 10, 20)
# # X, Y = np.meshgrid(x_val, y_val)
# #
# # # Evaluate the function on the grid of points
# # Z = X**2 + Y**2 + 5
# #
# # # Create a 3D plot
# # fig = plt.figure()
# # ax = fig.add_subplot(111, projection='3d')
# # ax.plot_surface(X, Y, Z)
# #
# # # Define light source
# # light_source = np.array([5, 5, 10])
# #
# # # Define normal vector of surface at the light source point
# # normal = np.array([2*light_source[0], 2*light_source[1], 1])
# #
# # # Normalize the normal vector
# # normal = normal / np.linalg.norm(normal)
# #
# # # Define the light direction
# # light_direction = np.array([-light_source[0], -light_source[1], -light_source[2]])
# # light_direction = light_direction / np.linalg.norm(light_direction)
# #
# # # Define the intensity of the light
# # intensity = 0.8
# #
# # # Calculate the dot product of the normal and light direction
# # dot_product = np.dot(normal, light_direction)
# #
# # # Calculate the diffuse reflection of the light
# # diffuse_reflection = dot_product * intensity
# #
# # # Add the diffuse reflection to the surface
# # ax.plot_surface(X, Y, Z + diffuse_reflection)
# #
# # # Add the light source and its direction
# # ax.scatter(light_source[0], light_source[1], light_source[2], color='r', marker='o')
# # ax.quiver(light_source[0], light_source[1], light_source[2], light_direction[0], light_direction[1], light_direction[2], color='r', arrow_length_ratio=0.3)
# #
# # # Add labels and show the plot
# # plt.xlabel('X')
# # plt.ylabel('Y')
# # plt.show()
# import numpy as np
# import matplotlib.pyplot as plt
#
# # Define the surface equation
# def surface(x_val, y_val):
#     return x_val**2 + y_val**2 + 5
#
# # Define a function to calculate the reflection vector
# def reflect(incident, normal):
#     return incident - 2 * np.dot(incident, normal) * normal
#
# # Define the source point and hit points
# source = np.array([1, 2, 3])
# hit_points = np.array([[-1, -2, surface(-1, -2)],
#                       [2, 3, surface(2, 3)],
#                       [-3, 4, surface(-3, 4)]])
#
# # Calculate the normals at the hit points
# normals = np.array([[-2*x_val, -2*y_val, -1] for x_val, y_val, z in hit_points])
#
# # Calculate the reflection vectors
# incident_vectors = hit_points - source[np.newaxis, :]
# reflection_vectors = reflect(incident_vectors, normals)
#
# # Plot the source point and hit points
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter(source[0], source[1], source[2], c='b', marker='o')
# ax.scatter(hit_points[:, 0], hit_points[:, 1], hit_points[:, 2], c='r', marker='o')
#
# # Plot the reflection vectors
# for i in range(len(hit_points)):
#     ax.quiver(hit_points[i, 0], hit_points[i, 1], hit_points[i, 2],
#               reflection_vectors[i, 0], reflection_vectors[i, 1], reflection_vectors[i, 2],
#               color='g')
#
# plt.show()
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the surface equation
def surface(x, y):
    return x**2 + y**2 + 5

# Define a function to calculate the reflection vector
def reflect(incident, normal):
    return incident - 2 * np.dot(incident, normal) * normal

# Define the source point and hit points
source = np.array([1, 2, 3])
hit_points = np.array([[-1, -2, surface(-1, -2)],
                      [2, 3, surface(2, 3)],
                      [-3, 4, surface(-3, 4)]])

# Calculate the normals at the hit points
normals = np.array([[-2*x, -2*y, -1] for x, y, z in hit_points])

# Calculate the reflection vectors
incident_vectors = hit_points - source[np.newaxis, :]
reflection_vectors = reflect(incident_vectors, normals)

# Create a 3D figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Generate data for the surface
X, Y = np.linspace(-5, 5, 100), np.linspace(-5, 5, 100)
X, Y = np.meshgrid(X, Y)
Z = surface(X, Y)

# Plot the surface
ax.plot_surface(X, Y, Z, cmap='viridis')

# Plot the source point and hit points
ax.scatter(source[0], source[1], source[2], c='b', marker='o')
ax.scatter(hit_points[:, 0], hit_points[:, 1], hit_points[:, 2], c='r', marker='o')

# Plot the reflection vectors
for i in range(len(hit_points)):
    ax.quiver(hit_points[i, 0], hit_points[i, 1], hit_points[i, 2],
              reflection_vectors[i, 0], reflection_vectors[i, 1], reflection_vectors[i, 2],
              color='g')

plt.show()
