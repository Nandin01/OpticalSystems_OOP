import numpy as np
import matplotlib.pyplot as plt


def illuminate(surface, light_pos, intensity):
    # surface is a 2D list of points
    # light_pos is a tuple  representing the position of the light source
    # intensity is a float representing the intensity of the light source

    # calculate the distance from each point on the surface to the light source
    distances = []
    for point in surface:
        distance = ((point[0] - light_pos[0]) ** 2 + (
                    point[1] - light_pos[1]) ** 2) ** 0.5
        distances.append(distance)

    # calculate the illumination at each point on the surface
    illuminations = []
    for distance in distances:
        illumination = intensity / (
                    distance ** 2 + 0.0001)  # add a small value to the denominator to avoid division by zero
        illuminations.append(illumination)

    return illuminations


# create a surface and a light source
surface = [[x, y] for x in range(-5, 6) for y in range(-5, 6)]
light_pos = (0, 0)
intensity = 100

# calculate the illumination at each point on the surface
illuminations = illuminate(surface, light_pos, intensity)

# plot the illumination pattern
plt.scatter([point[0] for point in surface], [point[1] for point in surface],
            c=illuminations)
plt.colorbar()
plt.show()