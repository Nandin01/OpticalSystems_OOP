#Strategy DP
import numpy as np

class Reflector:
    def __init__(self, incident, normal):
        self.incident = incident
        self.normal = normal

    def reflect(self):
        reflection = self.incident - 2 * (np.dot(self.incident, self.normal) / np.dot(self.normal, self.normal)) * self.normal
        return reflection

class NormalizedReflector(Reflector):
    def __init__(self, incident, normal):
        self.incident = normalize(incident)
        self.normal = normalize(normal)

def normalize(vector):
    return vector / np.linalg.norm(vector)


in1 = NormalizedReflector(np.array([1, 0]), np.array([1, 2]))
in2 = NormalizedReflector(np.array([1, 1]), np.array([1, 1.5]))
in3 = NormalizedReflector(np.array([0, 1]), np.array([1, 3]))

print(in1.reflect())
print(in2.reflect())
print(in3.reflect())