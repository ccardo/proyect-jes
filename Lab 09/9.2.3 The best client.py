##
#   best client exercise bammete

def best_customer_name(sales, names):

    namesSales = zip(names, sales)
    return max(namesSales)[0]


def main():

    sales = list()
    names = list()

    amount = int(input("Price of item: "))
    while amount != 0:
        name = input("Enter name of the client: ")
        sales.append(amount)
        names.append(name)
        amount = int(input("Price of item: "))

    nameOfBest = best_customer_name(sales, names)
    print(nameOfBest)
    
main()