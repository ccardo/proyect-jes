##
from csv import reader


def main():

    with open("driver_names.txt") as file_input:
        lines = file_input.readlines()
        stop_names_raw = [i.strip().split(": ") for i in lines if i.startswith("F")]
        driver_names_raw = [i.strip().split(": ") for i in lines if i.startswith("A")]
    driver_ids = {i[0]: i[1] for i in driver_names_raw}
    stop_ids = {i[0]: i[1] for i in stop_names_raw}

    passenger_activity = list(reader(open("turin_airport_data.csv")))
    header = passenger_activity[0]

    result_drivers = {driver_ids[id]: 0 for id in driver_ids}
    result_stops = {stop_ids[id]: [0, 0] for id in stop_ids}
    for stop in passenger_activity[1:]:

        driver_name = driver_ids[stop[0]]

        passengers_onboard = 0
        passengers_for_driver = [i for i in stop]
        for i, passengers in enumerate(passengers_for_driver):

            if "/" in passengers:
                passengers_onboard += 1
                passengers_for_driver[i] = int(passengers.split("/")[0]) - int(passengers.split("/")[1])
            if "--" in passengers:
                stop[i] = 0
                passengers_for_driver[i] = 0

        passengers = list(map(int, passengers_for_driver[2:]))
        passengers_onboard += sum([i for i in passengers if i > 0])
        result_drivers[driver_name] += passengers_onboard

        for i, passengers in enumerate(stop):
            if i < 2: continue
            stop_name = stop_ids[header[i]]

            if isinstance(passengers, str) and "/" in passengers:
                result_stops[stop_name][0] += int(passengers.split("/")[0])
                result_stops[stop_name][1] -= int(passengers.split("/")[1])
            elif int(passengers) > 0:
                result_stops[stop_name][0] += int(passengers)
            else:
                result_stops[stop_name][1] -= int(passengers)

    most_boarded_passengers = max(result_stops, key=lambda x: result_stops.get(x)[0])
    most_left_passengers = max(result_stops, key=lambda x: result_stops.get(x)[1])

    print(f"The stop at which the most passengers came onboard was {most_boarded_passengers}, with "
          f"{result_stops[most_boarded_passengers][0]} passengers.")
    print(f"The stop at which the most passengers left is {most_left_passengers}, with "
          f"{result_stops[most_left_passengers][1]} passengers.\n")

    top_drivers = sorted(result_drivers, key=result_drivers.get, reverse=True)
    print("Drivers with the most passengers onboard overall:\n")
    for i, driver in enumerate(top_drivers):
        if result_drivers[driver] == 0: continue
        print(f"{i+1}) {driver}, with {result_drivers[driver]} passengers.")


if __name__ == '__main__':
    main()