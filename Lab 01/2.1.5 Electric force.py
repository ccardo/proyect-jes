##
from math import *
#
q1 = float(input("insert value of the first charge [Coulomb]: "))
q2 = float(input("insert value of the second charge [Coulomb]: "))
r = float(input("what is the distance between the two charges? [meters] "))
epsilon = float(8.854 * (10 ^ (-12)))
#
# executes the operation for the Coulomb force between the charges
#
Force = (q1 * q2)/(4 * pi * (r**2) * epsilon)
print("the electrical force is: ", Force)
