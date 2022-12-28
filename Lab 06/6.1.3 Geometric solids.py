##
# this program defines functions for calculating
# volume and surface area of: Sphere, Cylinder, Cone

def sphereVolume(r):
    import math as m
    return 4 / 3 * m.pi * (r ** 3)


def sphereSurface(r):
    import math as m
    return 4 * m.pi * (r ** 2)


def cylinderVolume(r, h):
    import math as m
    return h * m.pi * (r ** 2)


def cylinderSurface(r, h):
    import math as m
    return 2 * m.pi * ((r ** 2) + h * r)


def coneVolume(r, h):
    import math as m
    return 1 / 3 * m.pi * (r ** 2) * h


def coneSurface(r, h):
    import math as m
    return m.pi * ((r ** 2) + r * m.sqrt(r ** 2 + h ** 2))


if __name__ == '__main__':
    radius = float(input('> radius = '))
    height = float(input('> height = '))
    print('%40s %60s' % ('Volume [u^3]', 'Surface [u^2]'))
    print(f'SPHERE{sphereVolume(radius):>40}{sphereSurface(radius):>60}')
    print(f'CYLINDER{cylinderVolume(radius, height):>38}{cylinderSurface(radius, height):>60}')
    print(f'CONE{coneVolume(radius, height):>42}{coneSurface(radius, height):>60}')
