##
# this function will calculate the necessary power
# for a car to overcome the air resistance, at a given speed

def main():
    velocity = float(input('> Velocity [m/s] = '))
    AIR_DENSITY = 1.23  # kg / m ** 3
    SURFACE_AREA = 2.5  # m ** 2
    CP = 0.2

    airResistance = 0.5 * AIR_DENSITY * SURFACE_AREA * CP * (velocity ** 2)
    equivalentPower = round(airResistance * velocity, 4)
    horsePower = round(equivalentPower / 745.7, 4)  # Hp

    print(f'Car power [W] = {equivalentPower:>10}')
    print(f'Car power [Hp] = {horsePower:>9}')

if __name__ == '__main__':
    main()
