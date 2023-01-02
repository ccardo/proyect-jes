##
#

def main():

    from pprint import pprint

    with open("products", "r") as file1, open("purchases", "r") as file2:
        official_sellers_list = [line.strip().split() for line in file1]
        purchases_list = [line.strip().split() for line in file2]

    official_sellers = {line[0]: line[1] for line in official_sellers_list}
    illegal_products = dict()
    for purchase in purchases_list:

        product = purchase[0]
        reseller = purchase[1]

        if reseller != official_sellers.get(product):
            if product not in illegal_products:
                illegal_products.update({product: {reseller}})
                continue
            illegal_products[product].add(reseller)

    print(f"Suspicious sales:\n")
    for key in illegal_products:
        print(f"Product: {key}")
        print(f"Reseller:", *illegal_products[key])
        print(f"Official reseller: {official_sellers[key]}\n")


if __name__ == '__main__':
    main()