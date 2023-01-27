#

def main():

    with open("foods.txt") as foods_file:
        foods_raw = [i.strip().split(";") for i in foods_file]
    foods_info = {i[0]: [float(i[1]), float(i[2])] for i in foods_raw}

    filename = input("insert file name: ") + ".txt"
    with open(filename) as fusilli_file:
        ricette_raw = [i.strip().split(";") for i in fusilli_file]
    ingredients = {}
    for i, line in enumerate(ricette_raw):
        if 0 < i < ricette_raw.index(["Procedimento:"]) - 1:
            ingredients[line[0]] = int(line[1])

    total_calories = 0
    total_cost = 0

    for ingredient in ingredients:
        quantity = ingredients[ingredient]
        total_calories += foods_info[ingredient][1] * quantity / 1000
        total_cost += foods_info[ingredient][0] * quantity / 1000

    print(f"{filename}:\n- total calories: {total_calories}\n- total cost: {total_cost}")


if __name__ == '__main__':
    main()