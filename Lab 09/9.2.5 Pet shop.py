##
#   pet shop pizello


def discount(prices, is_pet):

    if True not in is_pet:
        return "No discount"

    discounted = 0
    for i, n in enumerate(prices):
        if not is_pet[i]:
            discounted += n

    return discounted


def main():
    isPetList = list()
    pricesList = list()

    price = float(input("enter price: "))
    while price != -1:
        pricesList.append(price)

        isPet = input("is this a pet? (yes/no)").strip().lower().startswith('y')
        isPetList.append(isPet)

        price = float(input("enter price: "))

    scount = discount(pricesList, isPetList)
    print(f"total discount = {scount}")
    print(f"total amount (discounted) = {sum(pricesList) - scount}")

main()