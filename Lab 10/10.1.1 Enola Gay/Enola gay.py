##
#

def main():

    with open("input_enola_gay.txt", "r") as file:
        lines = file.readlines()

    with open("output_enola_gay.txt", "w") as output:

        for line, text in enumerate(lines):
            output.write(F"/*{line+1}*/ {text}")

if __name__ == '__main__':
    main()