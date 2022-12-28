##
#   given a list of flights, the program should display, once given departure and arrival city,
#   all the possible flights with at most 1 stop in the same day that take from the departure city to the arrival one.
#   the program should display: flight departure and arrival, flight cost and flight total time


def main():
    flights = create_flight_list()
    departureCity = input("Enter departure city:\n>").upper()
    destinationCity = input("Enter destination city:\n>").upper()

    directFlights = search_direct_flights(flights, departureCity, destinationCity)
    # check if the list directFlights is existent. Also works as a spellcheck
    if directFlights:
        print(f"\nDirect flight options:\n")
        print_flight(directFlights)
        print(f"Travelling time: {directFlights[0][4]}")
        print(f"Cost: {directFlights[0][2]} $\n")
    else:
        print("\nNo direct flights are available.\n")

    oneStopFlights = search_one_stop_flights(flights, departureCity, destinationCity)
    # check if the list oneStopFlights is existent. Also works as a spellcheck
    if oneStopFlights:
        print("One-stop flights:\n")
        for flightCouple in oneStopFlights:
            print_flight(flightCouple)

            hours0, minutes0 = calculate_time(flightCouple[0])[0], calculate_time(flightCouple[0])[1]
            hours1, minutes1 = calculate_time(flightCouple[1])[0], calculate_time(flightCouple[1])[1]

            # I feel like I'm always adjusting the time...
            if minutes0 + minutes1 < 60:
                travellingTime = f"0{hours0 + hours1}:{minutes0 + minutes1}"
            else:
                travellingTime = f"0{hours0 + hours1 + 1}:{minutes0 + minutes1 - 60}"

            print(f"Travelling time: {travellingTime}")
            print(f"Total price: {flightCouple[0][2] + flightCouple[1][2]} $\n")
    else:
        print("No one-stop flights are available.\n")


def create_flight_list():
    with open("flights.txt", "r") as file:

        all_flights_list = list()
        for flight in file:
            flight = flight.split(",")
            code = flight.pop(0)  # the flight code is relocated to the end of the list because it's useless

            # FLIGHT FORMAT: [[XX:YY, DEPARTURE CITY], [XX:YY, ARRIVAL CITY], Cost, Flight code, Travelling time]
            #                                                                                        ^^^^^^
            #                                                                                    gets added later
            all_flights_list.append(
                [
                    flight[0:2],
                    flight[2:4],
                    int(flight[4]),
                    code
                ]
            )

    return all_flights_list


def search_direct_flights(flights_list, departure, destination):

    # filters by departure and destination
    search_result = list(filter(lambda x: x[0][1] == departure and x[1][1] == destination, flights_list))
    for flight in search_result:

        hours, minutes = calculate_time(flight)[0], calculate_time(flight)[1]
        flight.append(f"0{hours}:{minutes}") if minutes > 9 else f"0{hours}:0{minutes}"

    return search_result


# this has 'arrival' as parameter because the flight doesn't land immediately at the destination
def search_one_stop_flights(flights_list, departure, arrival):

    import itertools as IT
    flights_list = list(IT.filterfalse(lambda x: x[0][1] == departure and x[1][1] == arrival, flights_list))

    flights_from_departure = list(filter(lambda x: x[0][1] == departure, flights_list))
    flights_to_arrival = list(filter(lambda x: x[1][1] == arrival, flights_list))

    search_result = list()
    for flight1 in flights_from_departure:
        time1 = int(flight1[1][0][:2])
        for flight2 in flights_to_arrival:
            time2 = int(flight2[0][0][:2])

            # if the destination of flight1 and departure of flight2 coincide
            # and the flights are on the same day, append each to search result in a tuple
            if flight1[1][1] == flight2[0][1] and time2 - time1 > 0:
                hours1, minutes1 = calculate_time(flight1)[0], calculate_time(flight1)[1]
                hours2, minutes2 = calculate_time(flight2)[0], calculate_time(flight2)[1]

                # append the travelling time (the zeros in front serve as a legibility tool)
                flight1.append(f"0{hours1}:{minutes1}") if minutes1 > 9 else f"0{hours1}:0{minutes1}"
                flight2.append(f"0{hours2}:{minutes2}") if minutes2 > 9 else f"0{hours2}:0{minutes2}"

                search_result.append((flight1, flight2))

    return search_result


def calculate_time(flight):

    # time 1 = xx:yy, time 2 = XX:YY
    # hours = (XX - xx):(YY - yy)
    hours = int(flight[1][0][:2]) - int(flight[0][0][:2])
    minutes = int(flight[1][0][3:]) - int(flight[0][0][3:])

    # adjust the time for negative minute difference (e.g. 02:30 - 01:50 = 00:40 -> would give 01:-20 without fix)
    if minutes < 0:
        minutes = 60 - abs(minutes)
        hours -= 1

    return hours, minutes


def print_flight(flights):

    for flight in flights:
        print(f"{flight[3]} {flight[0][1]} {flight[0][0]}  ->  {flight[1][1]} {flight[1][0]}")


if __name__ == '__main__':
    main()
