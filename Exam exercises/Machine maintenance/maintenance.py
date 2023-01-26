##
from csv import reader
from datetime import datetime

def main():

    parameters_list = list(reader(open("parameters.txt")))
    maintenance_dates_list = list(reader(open("maintenance_dates.txt")))

    parameters = {i[1]: i[0] for i in parameters_list}
    maintenance_dates = {i[1]: [i[0], i[2]] for i in maintenance_dates_list}

    for parameter in parameters:

        day, month, year = tuple(map(int, parameters[parameter].split("/")))
        comparison_date = datetime(year, month, day); print("--"*47)
        param = "before" if parameter == "a" else "after"

        operations = []
        for date in maintenance_dates:

            comp_day, comp_month, comp_year = tuple(map(int, date.split("/")))
            current_date = datetime(comp_year, comp_month, comp_day)

            if comparison_date > current_date and param == "before":
                operations.append([date, maintenance_dates[date][0], maintenance_dates[date][1]])

            elif comparison_date < current_date and param == "after":
                operations.append([date, maintenance_dates[date][0], maintenance_dates[date][1]])

        print(f"Operations done {param} {parameters[parameter]}:\n")
        for operation in operations:
            print(f"\t{operation[1]} occurred on {operation[0]}, costed {operation[2]}$.")

        most_expensive = max(operations, key=lambda x: int(x[2]))
        print(f"\nThe most expensive operation was: {most_expensive[1]}"
              f" on the day {most_expensive[0]}, having costed {most_expensive[2]}$.")
        print("--" *47)


if __name__ == '__main__':
    main()