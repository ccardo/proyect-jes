
def create_flight_list():

    """returns a list of the flights"""

    with open("flights.txt", "r") as file:

        flightsList = [i.strip().split(",") for i in file.readlines()]

    return flightsList


def search_direct_flights(flight_list, departure, arrival):

    """prints a list of direct flights that correspond
    to the given departure and arrival cities"""

    print("\nDirect flights:\n")
    for i in flight_list:
        if i[2] == departure and i[4] == arrival:

            hours, minutes = calculate_time(i[1], i[3])
            print(f"{i[0]}  {i[2]} {i[1]} -> {i[4]} {i[3]}\nTime {hours}:{minutes}\nPrice: {i[5]}£")


def search_one_stop_flights(flight_list, departure, arrival):

    """prints a list of flights that start at the departure city
    and end at the arrival city, but have one stop in the middle:
    The second flight has to:
    - be within 24 hours of the first one
    - be at least 30 minutes after the first one"""

    from itertools import filterfalse
    flight_list = list(filterfalse(lambda x: x[2] == departure and x[4] == arrival, flight_list))

    print("\nOne-stop flights:\n")
    for flight1 in flight_list:
        if flight1[2] == departure:

            hours1, minutes1 = calculate_time(flight1[1], flight1[3])

            for flight2 in flight_list:
                if flight2[4] == arrival and flight2[2] == flight1[4]:

                    hours2, minutes2 = calculate_time(flight2[1], flight2[3])
                    differenceHours, differenceMinutes = calculate_time(flight1[3], flight2[1])
                    totalHours, totalMinutes = calculate_time(flight1[1], flight2[3])

                    if (minutes2 - minutes1 > 30 or differenceHours > 0) and differenceHours > 0:
                        print(f"{flight1[0]}  {flight1[2]} {flight1[1]} -> {flight1[4]} {flight1[3]}")
                        print(f"{flight2[0]}  {flight2[2]} {flight2[1]} -> {flight2[4]} {flight2[3]}")
                        print(f"Total traveling time {totalHours}:{totalMinutes}")
                        print(f"Total cost: {int(flight1[5]) + int(flight2[5])}£\n")


def calculate_time(time1, time2):

    """calculates the time between two given hours:minutes
    by transforming the hours and minutes in seconds and subtracting them

    :returns tuple with difference hours and minutes"""

    time1List = time1.split(":")
    time2List = time2.split(":")

    Mins2 = int(time2List[1]) + int(time2List[0])*60
    Mins1 = int(time1List[1]) + int(time1List[0])*60

    totalMins = Mins2 - Mins1

    hours = totalMins // 60
    minutes = totalMins % 60

    return hours, minutes


def main():

    allFlights = create_flight_list()
    departure = input("insert departure city\n>").upper()
    arrival = input("insert arrival city\n>").upper()

    search_direct_flights(allFlights, departure, arrival)
    search_one_stop_flights(allFlights, departure, arrival)


if __name__ == '__main__':
    main()
