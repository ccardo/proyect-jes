##
#

def main():

    # open and read the file
    file_path = "values.txt"
    with open(file_path, "r") as file:
        lines = [i.split() for i in file]

    # pick the instances where the blood sugar > 200
    max_value = 200
    patients_at_risk = {}
    for patient in lines:

        code = patient[0]
        sugar_value = patient[2]

        if int(sugar_value) >= max_value:

            if code not in patients_at_risk:
                patients_at_risk[code] = [sugar_value]
            else:
                patients_at_risk[code].append(sugar_value)

    # sort the excesses by the number of instances in which they occurred
    sorted_by_criticality = sorted(patients_at_risk.items(), key=lambda x: len(x[1]), reverse=True)

    # print the desired patient info
    for patient in sorted_by_criticality:
        print()
        for patient_info in lines:

            if patient[0] == patient_info[0] and patient_info[2] in patient[1]:

                print(f"{patient_info[0]} {patient_info[1]} {patient_info[2]}")


if __name__ == '__main__':
    main()
