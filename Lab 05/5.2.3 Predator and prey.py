##
# this code simulates the natural behavior of predator and prey
# through some mathemtical equations

def main():
    grPrey = float(input(f'{"> Growth rate of prey: ":<70}'))
    destPrey = float(input(f'{"> Mortality rate of prey (through predator consumption): ":<70}'))
    grPredator = float(input(f'\n{"> Growth rate of predators (through prey consumption): ":<70}'))
    destPredator = float(input(f'{"> Mortality rate of predators: ":<70}'))
    prey = int(input(f'\n{"> Prey population: ":<40}'))
    predators = int(input(f'{"> Predator population: ":<40}'))
    timePeriod = int(input(f'{"> Number of time periods to consider: ":<40}'))

    for i in range(timePeriod):
        prey = round(prey * (1 + grPrey - destPrey * predators), 2)
        predators = round(predators * (1 - destPredator + grPredator * prey), 2)

    print(f'\nFinal prey population: {prey}')
    print(f'Final predator population: {predators}')


if __name__ == '__main__':
    main()
