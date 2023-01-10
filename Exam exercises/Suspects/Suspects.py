##
#
import csv


def main():

    with open("suspects.txt", "r") as suspects_file:
        suspects = [i.strip() for i in suspects_file]

    with open("presences.txt", "r") as presences_file:
        presences = {}
        for line in presences_file:
            data = line.strip().split(", ")
            presences.update({data[0]: data[1:]})

    for suspect in suspects:

        print(f"Contacts of {suspect}:")
        contacts = list()

        if suspect not in presences:
            print(f"\t* Client {suspect} not in archive.")
            continue

        for name in presences:

            if suspect == name:
                continue
            if int(presences[suspect][1]) > int(presences[name][2]):
                continue
            if int(presences[suspect][2]) < int(presences[name][1]):
                continue

            contacts.append((name, presences[name][0]))

        if not contacts:
            print(f"\t* {suspect} has had no contacts in this time window.")
            continue
        for contact in sorted(contacts, key=lambda x: x[0]):
            print(f"\t* Contact with {contact[0]}, phone {contact[1]}")


if __name__ == '__main__':
    main()
