##
year = int(input("what year is it in your timeline? "))
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a leap year")
    exit("hehe")

else:
    print(year, "is not a leap year")
