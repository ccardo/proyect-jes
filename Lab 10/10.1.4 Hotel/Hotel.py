##
#

def main():

    try:
        with open("input.txt", "r") as file:

            lines = file.readlines()
            lines = [line.strip().lower().split(";") for line in lines]
            info = dict()

            for line in lines:

                if line[1] not in info:
                    prices = set()
                elif line[1] in info:
                    prices = info.get(line[1])
                prices.add(float(line[2]))
                info.update({line[1]: prices})

    except IOError:
        exit("The file doesn't exist, or the format is incorrect.")

    for key in info:

        times = len(info[key])
        totalPrice = sum(info[key])
        print(f'The service "{key.capitalize()}"'
              f' has been utilized {times}'
              f' times for a total of {totalPrice}$.')

if __name__ == '__main__':
    main()



