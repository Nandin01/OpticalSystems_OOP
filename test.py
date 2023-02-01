# python OOP
class Reflector:
    num_of_ref = 0  # class variable
    rejection_amount = 1

    def __init__(self, incident, reflection, fraction):
        self.incident = incident  # instance variable
        self.reflection = reflection
        self.fraction = fraction
        self.test = incident + reflection

        Reflector.num_of_ref += 1

    def reflector(self):
        return "{} {}".format(self.incident, self.reflection)

    def reflector_test(self):
        return "{}".format(self.test)

    def fraction_calc(self):
        self.fraction = int(self.fraction * self.rejection_amount)
        return self.fraction

    @classmethod
    def change_rejection(cls, reject):
        cls.rejection_amount = reject


jk = Reflector(0, 1, 4)
jl = Reflector(1, 1, 3)
Reflector.change_rejection(1.5)
# What would I implement but can be replaced with function
# print("{} {}".format(jk.incident, jk.reflection))
print(jk.test)
print(jk.fraction_calc())
print(jk.rejection_amount)
# Count total reflection
# print(Reflector.num_of_ref)

