# OOP refraction
import math

import numpy as np

class Refraction:
    def __init__(self, n1, n2, incident, normal):
        self.n1 = n1
        self.n2 = n2
        self.incident = incident
        self.normal = normal

    def refract(self):
        r1 = ((self.n1 / self.n2) * self.incident) - ((self.n1 / self.n2) * (
            self.incident.dot(self.normal)) + math.sqrt(1 - ((self.n1 / self.n2) ** 2) * (1 - (self.normal.dot(self.incident)) ** 2))) * self.normal
        return r1
# normalize self.incidence

n1 = 1.0
n2 = 1.5
# ins = np.array([0, 1])
# norm = np.array([1, 0])

def normalize(vector):
    return vector / np.linalg.norm(vector)
# vector = normalize(np.array([1,3]))
# print(vector)
# jk = normalize(np.array([0,3]))
# print(jk)
in1 = Refraction(1, 1.5, normalize(np.array([1,0])), normalize(np.array([1,2])))
# normalized_in1 = in1 / np.linalg.norm(in1)
in2 = Refraction(0.5, 1, normalize(np.array([1,1])), normalize(np.array([1,1.5])))
# Create an instance of Refraction class
# ref = Refraction(n1, n2, ins, norm)
#
# # Compute the refaction vector
# refraction = ref.refract()
print(in1.refract())

        


