##
#

def main():

    file_path = "Exam exercises/Glucometer/values.txt"
    with open(file_path, "r") as file:
        lines = [i.split() for i in file]
    
    print(*lines, sep="\n")

    max_value = 200
    exceedances = {}
    for patient in lines:

        code = patient[0]
        sugar_value = int(patient[2])

        if sugar_value > max_value:

            if code not in exceedances:
                exceedances[code] = {int(sugar_value)}
            else:
                exceedances[code].add(sugar_value)

    for patient in lines:

        if any(x[2] in exceedances[x[0]] for x in lines):

            print(patient[0], patient[1], patient[2])


main()