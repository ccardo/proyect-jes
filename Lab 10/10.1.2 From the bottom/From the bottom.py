##
#

def main():

    with open("input_from_the_bottom.txt", "r") as file:

        lines = file.readlines()
        lines.reverse()

    with open("output_from_the_bottom.txt", "w") as output:
        for line in lines:
            output.write(line)

if __name__ == '__main__':
    main()