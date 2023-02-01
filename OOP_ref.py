# import numpy as np
# class Reflector:
#
#     def __init__(self, incident, normal):
#         self.incident = incident
#         self.normal = normal
#
#     def reflect(self):
#         reflection = self.incident - 2 * (
#                     np.dot(self.incident, self.normal) / np.dot(self.normal,
#                                                                 self.normal)) * self.normal
#         return reflection
#
#
# # Define the incident and normal vectors
# incident1 = np.array([1, 0])
# normal1 = np.array([1, 1])
#
#
# def normalize(vector):
#     return vector / np.linalg.norm(vector)
#
#
# in1 = Reflector(normalize(np.array([1, 0])), normalize(np.array([1, 2])))
# # normalized_in1 = in1 / np.linalg.norm(in1)
# in2 = Reflector(normalize(np.array([1, 1])), normalize(np.array([1, 1.5])))
# in3 = Reflector(normalize(np.array([0, 1])), normalize(np.array([1, 3])))
#
# print(in1.reflect())

#Flyweight DP
import numpy as np

class Reflector:
    def __init__(self, incident, normal):
        self.incident = incident
        self.normal = normal
    def reflect(self):
        reflection = self.incident - 2 * (np.dot(self.incident, self.normal) / np.dot(self.normal, self.normal)) * self.normal
        return reflection

class ReflectorFlyweightFactory:
    def __init__(self):
        self._flyweights = {}
    def get_flyweight(self, incident, normal):
        key = self._get_key(incident, normal)
        if key not in self._flyweights:
            self._flyweights[key] = Reflector(incident, normal)
        return self._flyweights[key]
    def _get_key(self, incident, normal):
        return str(incident) + '_' + str(normal)

def normalize(vector):
    return vector / np.linalg.norm(vector)

factory = ReflectorFlyweightFactory()

in1 = factory.get_flyweight(normalize(np.array([1, 0])), normalize(np.array([1, 2])))
in2 = factory.get_flyweight(normalize(np.array([1, 0])), normalize(np.array([1, 2])))
in3 = factory.get_flyweight(normalize(np.array([0, 1])), normalize(np.array([1, 3])))

print(in1.reflect())
print(in2.reflect())
print(in3.reflect())
