##
import math
G = 6.67 * 10**(-11)
d = 9400
r = d/2
M = 2.2 * 10**14
vEscape = math.sqrt(2 * G * M / r)

LaunchSpeed = float(input('Insert a launch speed [m/s]: '))
if LaunchSpeed > vEscape:
    print('paittisti cumpa')
    necessaryMass = (LaunchSpeed ** 2 * r) / (G * 2)
    massDifference = necessaryMass - M
    print('to return to the comet\'s surface, it would need', massDifference, 'more kg of mass.')
else:
    print('your speed is not sufficient to leave the surface of the Earth.')

exit()
