##
#

def main():

    CSC1 = [["CSC1"]] + read_lines("CSC1.txt")
    CSC2 = [["CSC2"]] + read_lines("CSC2.txt")
    MTH121 = [["MTH121"]] + read_lines("MTH121.txt")

    classes = [CSC1, CSC2, MTH121]
    userInput = input("Insert student code:\n>")
    profile = student_profile(userInput, classes)

    if len(profile) > 1:
        for key in profile:
            print(f"│{f'{key}:':<10}{profile.get(key):>5}│")
    else:
        print("There is no student with this code in our database.")


def read_lines(file):
    with open(file, "r") as file:
        lines = file.readlines()
    return [i.strip().split() for i in lines]


def student_profile(student_code, files):
    profile = dict({"Student": student_code})
    for single_class in files:
        for student in single_class:
            if student[0] == student_code:
                profile.update({single_class[0][0]: student[1]})
    return profile

main()
