##
#
from pprint import pprint
from colorama import Fore, init
init()  # initialize colorama

def main():

    try:
        with open("/Users/riccardo/VSCode Projects/proyect-jes/Exam exercises/Magic fruit boxes/actions.txt", "r") as file:
            lines = list(map(str.strip, file.readlines()))
    except IOError:
        exit("Error: no file with that name has been found.")

    actions = []
    magic_fruit_boxes = {}
    for line in lines:

        split_line = line.split()
        action = split_line[1]
        fruit = split_line[3]

        try:

            match action:                                                           # substitute to the if-else chain
                case "gives" if fruit not in magic_fruit_boxes:                     # looks cleaner in my opinion
                    magic_fruit_boxes.update({fruit: 1})

                case "gives" if len(sorted(magic_fruit_boxes)) > 42:                # raises IndexError if the total n.
                    raise IndexError                                                # of boxes is > than the max (42)

                case "gives":
                    magic_fruit_boxes[fruit] += 1

                case "takes":                                                       # raises KeyError if the fruit is
                    magic_fruit_boxes[fruit] -= 1                                   # not in the dictionary
                    if magic_fruit_boxes.get(fruit) == 0:                           # (there is no box of that fruit)
                        magic_fruit_boxes.pop(fruit)

        except IndexError:
            print(f"{Fore.RED}Alice could not take a {fruit}: magic boxes full{Fore.RESET}")
        except KeyError:
            print(f"{Fore.RED}Alice could not give a {fruit}: fruit not in stock{Fore.RESET}")
        else:
            name = "Bob" if action == "gives" else "Carl"
            actions.append(f"{name} {action} a {fruit}")
    print(*actions, sep="\n")

    if len(lines) == len(actions):
        print("\nAll OK.")

    print("\nSorted list of fruit magic boxes:")
    for fruit in sorted(magic_fruit_boxes, key=magic_fruit_boxes.get, reverse=True):
        print(f"{fruit:<15}{magic_fruit_boxes[fruit]:>5}")


if __name__ == '__main__':
    main()
