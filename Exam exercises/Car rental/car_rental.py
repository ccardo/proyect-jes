##
from csv import reader


def main():

    car_list = list(reader(open("cars.csv")))[1:]

    categories = {i[0]: [] for i in car_list}
    for car in car_list:
        categories[car[0]].append(car[1:])

    desired_category = input("Input category and days, separated by spaces: ").casefold()
    user_info = desired_category.split()
    days, car_type = user_info[1:], user_info[0]

    cars_category = categories[car_type] if car_type in categories else \
        exit(f'We haven\'t got any "{car_type}" cars in stock - try again.')
    n = 1
    for car in cars_category:
        try:
            if not days: raise ValueError
            if all(car[int(day) + 2] == "L" for day in days):
                print(f"\n\t{n}) {car[0]} {car[1]}, color:'{car[2]}'")
        except IndexError:
            exit("Please insert valid days on which to rent the car.")
        except ValueError:
            exit("Please insert valid days on which to rent the car.")


if __name__ == '__main__':
    main()