##
#

def main():

    with open("values.txt") as file:
        values = [i.strip().split() for i in file]

    max_value = 200
    patients_at_risk = {i[0]: [] for i in values if float(i[2]) >= max_value}
    for i in values:
        patient_id = i[0]
        if float(i[2]) >= max_value:
            patients_at_risk[patient_id].append(i[1:])

    for patient_id in sorted(patients_at_risk, key=lambda x: len(patients_at_risk[x]), reverse=True):
        for report in patients_at_risk[patient_id]:
            print(patient_id, *report, sep=" ")
        print()

if __name__ == '__main__':
    main()