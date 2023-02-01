import numpy as np

# def reflect(incident, normal):
#
#     # reflection = np.dot(incident, normal) * normal
#     reflection = incident-2*(incident*normal)*normal
#     # subtract the projection from the incident vector to get the rejection
#     # rejection = incident - reflection
#
#     # the reflection vector is just the negative of the rejection
#     # reflection = -rejection
#
#     return reflection
# incident1 = np.array([1, 0])
# normal1 = np.array([1, 1])
#
#
# reflection = reflect(incident1, normal1)
#
# print(reflection)
def reflect(incident, normal):
    normal_magnitude = np.linalg.norm(normal)
    reflection = incident - 2*(np.dot(incident, normal)/normal_magnitude**2) * normal
    return reflection

incident1 = np.array([1, 0])
normal1 = np.array([1, 1])

reflection = reflect(incident1, normal1)

print(reflection)