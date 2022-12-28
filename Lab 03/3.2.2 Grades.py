##
grade = str(input("WHAT'S YOUR GRADE IN AMERICA?"))
plus = minus = 0.3
operators = "+", "-"
if "a" or "A" in grade:
    gradenum = 3.7
elif "b" or "B" in grade:
    gradenum = 2.7
elif "c" or "C" in grade:
    gradenum = 1.7
elif "d" or "D" in grade:
    gradenum = 0.7
elif "f" or "F" in grade:
    gradenum = 0

if "+" in grade:
    # noinspection PyUnboundLocalVariable
    voto = float(gradenum) + 0.3
    print(voto)
if "-" in grade:
    voto = float(gradenum) - 0.3
    print(voto)
