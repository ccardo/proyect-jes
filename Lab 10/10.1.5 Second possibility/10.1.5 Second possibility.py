##
#

def main():

    number_list = list()

    userInput = 0
    retries = 0
    while userInput != "":
        try:
            number_list.append(float(userInput))
            retries = 0
            userInput = input("Insert float value: ")

        except ValueError:
            if retries == 2:
                exit("Too many invalid value types.")
            retries += 1
            print(f"Incorrect value type. "
                  f"Try again ({2 - retries}"
                  f" retries left):\n")

    if sum(number_list):
        print(f"Sum of list: {sum(number_list)}")

if __name__ == '__main__':
    main()
