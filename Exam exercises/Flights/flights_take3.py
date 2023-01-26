##
import csv

def main():

    flights = list(csv.reader(open("flights.txt")))

    departure = input("Insert departure city: ").upper()
    arrival = input("Insert arrival city: ").upper()

    direct_flights = search_direct_flights(flights, departure, arrival)
    for i in direct_flights:
        print_flight(i, calculate_time(i[1], i[3]), i[5])
    
    print("\nOne-stop flights:")
    search_flights_with_change(flights, departure, arrival)

def print_flight(flight, time, cost):
    print(f"{flight[0]}  {flight[2]} --> {flight[4]}:")
    if time:
        print("total time:", f"{time[0]}:{time[1]}")
    if cost:
        print("total cost:", cost)


def search_flights_with_change(flights, start, end):

    possible_flights = [i for i in useful_flights(flights, start, end) 
    if i not in search_direct_flights(flights, start, end)]

    for i in possible_flights:
        
        arrival_time_1 = i[3]
        departure_time_1 = i[1]

        change_flights = useful_flights(flights, i[4], end)
        for j in change_flights:
            
            if j[4] != end:
                continue
            arrival_time_2 = j[3]
            departure_time_2 = j[1]

            difference_time_minimum = calculate_time(arrival_time_1, departure_time_2)
            difference_time_maximum = calculate_time(departure_time_1, arrival_time_2)
            
            if  difference_time_minimum[1] < 30 or difference_time_minimum[0] < 0:
                continue
            if not 0 < difference_time_maximum[0] < 24:
                continue
            
            print()
            print_flight(i, "", "")
            print_flight(j, "", "")
            print("total time:", f"{difference_time_maximum[0]}:{difference_time_maximum[1]}")
            print("total cost:", int(j[5]) + int(i[5]))
                
def useful_flights(flights, start, end):
    return [i for i in flights if i[2] == start]
            

def search_direct_flights(flights, start, end):
    return [flight for flight in flights if flight[2] == start and flight[4] == end]


def calculate_time(time_1, time_2):

    hours_1, minutes_1 = tuple(map(int, time_1.split(":")))
    hours_2, minutes_2 = tuple(map(int, time_2.split(":")))

    time_difference = (hours_2 *60 + minutes_2) - (hours_1 * 60 + minutes_1)

    result_hours = time_difference // 60
    result_mins = time_difference % 60

    return result_hours, result_mins

if __name__ == "__main__":
    main()