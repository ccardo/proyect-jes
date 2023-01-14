##
#
import csv


def get_list(file, roommate_list=None):
    lines = list(csv.reader(open(file)))
    if roommate_list is not None:
        return {line[0]: int(line[1]) for line in lines}

    return {line[0]: [lines.count(line), float(line[1]) * lines.count(line)] for line in lines}


def main():

    receipt = get_list("receipt.csv")
    roommate_list = get_list("roommate_list.csv", roommate_list=True)
    total = sum([int(receipt[item][1]) for item in receipt])

    print("\nItems not bought by the roommate:")
    due_money: float = 0.0
    for item, count in roommate_list.items():

        missing_item_count: float = 0.0
        try:
            item_count_in_receipt = receipt[item][0]
            total_price_in_receipt = receipt[item][1]
            
            if item_count_in_receipt < count:
                missing_item_count = count - item_count_in_receipt
                due_money += total_price_in_receipt
                print(f"\t* {item} - {missing_item_count}")
            else:
                due_money += total_price_in_receipt / item_count_in_receipt * count

        except KeyError:
            print(f"\t* {item} - {count};")

    print(f"\nDue money: {due_money} $")
    print(f"Total expense: {total} $")


if __name__ == '__main__':
    main()
