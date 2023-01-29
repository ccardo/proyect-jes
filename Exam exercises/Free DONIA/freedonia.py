##
import datetime

def main():

    filename_rules, filename_dates = "rules_big.txt", "dates_big.txt"
    with open(filename_rules) as file_rules:
        raw_rules = [i.strip().split(": ") for i in file_rules]
        rules_dates = {i[0]: i[1].split() for i in raw_rules}

    with open(filename_dates) as file_dates:
        requested_dates = [list(map(int, i.split("-"))) for i in file_dates]

    for request in requested_dates:

        active_rules = set()
        requested_date = datetime.date(*reversed(request))
        requested_date_str = "/".join(map(str, request))

        for date in rules_dates:
            current = list(map(int, date.split("-")))
            current_date = datetime.date(*reversed(current))
            if current_date > requested_date: break

            rules_added = {i.strip("+") for i in set(filter(lambda x: x.startswith("+"), rules_dates[date]))}
            rules_removed = {i.strip("-") for i in set(filter(lambda x: x.startswith("-"), rules_dates[date]))}

            active_rules = active_rules.union(rules_added)
            active_rules = active_rules.difference(rules_removed)

        print(f"\nActive rules on day {requested_date_str}:", *sorted(active_rules), sep="\n")


if __name__ == '__main__':
    main()