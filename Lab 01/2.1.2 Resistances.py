##
# insert the three resistances r1, r2, r3; r2 and r3 are connected in parallel, r1 in series.
#
r1 = int(input("First resistance: "))
r2 = int(input("Second resistance: "))
r3 = int(input("Third resistance: "))
#
# calculates the parallel sum and the total sum of the resistances
#
ResistanceSumParallel = (r2*r3)/(r2+r3)
ResistanceSumTotal = r1 + ResistanceSumParallel
#
# prints out the total resistance
#
print("The total resistance of the circuit is: ", ResistanceSumTotal)
