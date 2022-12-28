##
# the program calculates the total cost of a car after 5 years
#
CarType = input("Is your car Hybrid or Gasoline?")
NewCarCost = float(input("what's the cost of a new car? insert it here! "))
KmInAYear = 30000
FuelPrice = float(input("according to your knowledge, what is the estimate price for car fuel? "))
EfficiencyKmLiter = float(input("What is the car efficiency, calculated in Km/l? "))
#
# I estimate that the resale value after 5 years will be half of the total
# if the car is hybrid, it's likely its value won't fall off much
# Viceversa in the case of a gasoline car
#
if CarType == "hybrid" or "Hybrid":
    EstResaleValue = NewCarCost/2
elif CarType == "Gasoline" or "gasoline":
    EstResaleValue = NewCarCost/4
else:
    print("Insert a valid car type. Reset the program and retry.")
#
# calculates the cost of fuel for 1 year of usage
#
FuelLitersYearly = KmInAYear/EfficiencyKmLiter
FuelCostTotalYearly = FuelPrice * FuelLitersYearly
#
# calculates the whole cost of the car for 5 years, taking into account the car price
#
TotalCarUsageCost = (FuelCostTotalYearly + NewCarCost)*5
print("The total cost for a", CarType, "car, in 5 years of use, is:", TotalCarUsageCost)
# noinspection PyUnboundLocalVariable
print("The resale value of the car, after 5 years, is:", EstResaleValue)

