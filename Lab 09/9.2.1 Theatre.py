##
#   theatre - read a list with all the theater seats listed in the 9.2.1 theater.txt file
#   each seat is marked by a listed price. each time someone buys the seat, mark the seat with a 0
#   if someone searches for a price, highlight all the seats with that price.
from colorama import init, Fore
init()


class Theater:

    def __init__(self):
        self._occupied = None
        self._theaterSeats = []
        self._highlightedSeats = []

    # effectively creates the theater and stores it into self._theaterSeats (list)
    def create(self, file):
        with open(file, "r") as file:
            __LINES = file.readlines()
            __LINES = [i.strip() for i in __LINES]

            self._theaterSeats = list(map(lambda x: x.replace(", ", " ").split(), __LINES))
            return self._theaterSeats

    # prints seats, highlighted for when a price is highlighted;
    # occupied for when a selected seat is already occupied
    # (displays occupied seat in red)
    def printSeats(self, highlighted=False, occupied=False):

        state = self._theaterSeats
        if highlighted:
            state = self._highlightedSeats
        elif occupied:
            state = self._occupied

        for num, row in enumerate(state):
            for col in row:
                print(f"{col:<3}", end=' ')
            print(f"{Fore.LIGHTBLACK_EX}{num+1}{Fore.RESET}")

        for i in range(10):
            print(f"{Fore.LIGHTBLACK_EX}{i+1:<3}{Fore.RESET}", end=" ")

    # method that marks a picked seat with "XX"; returns None if utilized correctly, value_error if any other value than
    # 'int' is passed, returns index_error if the passed values are out of range
    def pickSeat(self, row, col):
        try:
            a = int(row)
            b = int(col)
            if not self._theaterSeats[a - 1][b - 1].isdigit():
                return "occupied"
            self._theaterSeats[a - 1][b - 1] = Fore.GREEN + 'XX ' + Fore.RESET

        except IndexError:
            return "index_error"
        except ValueError:
            return "value_error"

    # marks every seat with the desired price in a specific color,
    # changing the color as the price changes
    def highlightPrice(self, prices: list):

        colorsList = {
            "0": Fore.LIGHTCYAN_EX,
            "1": Fore.LIGHTGREEN_EX,
            "2": Fore.LIGHTYELLOW_EX,
            "3": Fore.LIGHTRED_EX,
            "4": Fore.LIGHTMAGENTA_EX
        }

        self._highlightedSeats[:] = [i[:] for i in self._theaterSeats]
        for row in self._highlightedSeats:
            for num, price in enumerate(prices):
                color = colorsList[str(num)]
                if price in row:
                    for index, seat in enumerate(row):
                        if seat in price:
                            row[index] = f"{color}{seat} {Fore.RESET}"

        self.printSeats(highlighted=True)

    # displays occupied seats in red
    def occupied(self):
        self._occupied = [i[:] for i in self._theaterSeats]
        for row in self._occupied:
            for index, seat in enumerate(row):
                if not seat.isdigit():
                    row[index] = Fore.RED + seat + Fore.RESET
        self.printSeats(occupied=True)


# main func
def main():

    theater = Theater()
    theater.create("9.2.1 theater.txt")
    print()
    theater.printSeats()

    while True:

        QUIT = input("\nQuit program? (YES/NO)").upper().startswith("Y")
        if QUIT:
            break
        chose_seat = input("Type whichever you want: a price or a seat = ").strip().lower().startswith("s")
        chose_price = not chose_seat

        if chose_seat:

            seat = input("\nType row and column of the seat, separated by a comma (Ex: a, b):\n> ")

            rowColumn = seat.split(",")
            if len(rowColumn) < 2:
                print("Use a comma to separate the digits. Try again.")
                continue
            row, column = rowColumn[0], rowColumn[1]
            errorIndicator = theater.pickSeat(row, column)

            if errorIndicator is None:
                theater.pickSeat(row, column)
                theater.printSeats(highlighted=False)

            if errorIndicator == "value_error":
                print("\nInvalid values. Try again.\n")
            if errorIndicator == "index_error":
                print("\nInvalid row or column. Try again.\n")
            if errorIndicator == "occupied":
                print("\nSeat is already occupied. Try again.\n")
                theater.occupied()

        elif chose_price:
            price = input("\nInsert price range of the seats you're looking for (price1, price2, ...)\n"
                          "If only 1 price desired, no need to input other prices - \n> ")
            priceList = [i.strip() for i in price.split(",")]
            theater.highlightPrice(priceList)


if __name__ == '__main__':
    main()
