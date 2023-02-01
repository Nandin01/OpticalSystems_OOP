# 2x^2-5x+3=0
from math import sqrt
# x_val= 1.5
# # Initial start
#
# # Loop until obtain solution
# for iteration in range(1,101):
#     xnew= (2*x_val**2+3)/5
#     # print(iteration, x_val)
#     if abs(xnew-x_val) < 0.000001:
#         break
#     x_val= xnew
# print("The root : %0.5f" % xnew)
# print("The number of iterations : %d" % iteration)

# While loop
x=5
xnew=0
iteration= 0
while abs(xnew-x) >= 0.000001:
    iteration += 1
    # we give the xnew value to x_val
    x = xnew
    xnew= (2*x**2+3)/5

print("The root : %f" % xnew)
print("The number of iterations : %d" % iteration)


