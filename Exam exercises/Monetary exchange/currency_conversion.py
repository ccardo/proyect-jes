##

def main():

    with open("conversions.txt") as conversion_file, open("iphone13mini.txt") as iphone_file:
        conversions = {i.split()[0]: float(i.split()[1]) for i in conversion_file}
        raw = [i.strip().split(";") for i in iphone_file]
        prices = {i[0]: i[1:] for i in raw}

    new_prices = {}
    for country in prices:

        currency = prices[country][0]
        if currency == "EUR": continue
        price: int = int(prices[country][1])

        new_price = round(price * conversions[currency], 2)
        new_prices[country] = new_price

    cheapest_country = min(new_prices, key=new_prices.get)
    print(f"The country in which the iPhone 13 Mini is the least expensive is: {cheapest_country}")
    print(f"Price: {new_prices[cheapest_country]} euros")


if __name__ == '__main__':
    main()