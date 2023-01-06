##
# This code formats the output of exercise 2.1.1 into a vertical column
Num1 = int(input("first number: "))
Num2 = int(input("second number: "))

# evaluates the operations using the numbers input by the user
# and assigns a title for each one of them
sum1, title1 = Num1 + Num2, 'Sum:'
diff, title2 = Num1 - Num2, 'Difference:'
prod, title3 = Num1 * Num2, 'Product:'
avg, title4 = (Num1 + Num2) / 2, 'Average:'
dist, title5 = abs(Num1 - Num2), 'Distance:'
maxN, title6 = max(Num1, Num2), 'Maximum:'
minN, title7 = min(Num1, Num2), 'Minimum:'

# prints out the results and titles in a column format
print("\n")
print("%-15s %15d" % (title1, sum1))
print("%-15s %15d" % (title2, diff))
print("%-15s %15d" % (title3, prod))
print("%-15s %15.1f" % (title4, avg))
print("%-15s %15d" % (title5, dist))
print("%-15s %15d" % (title6, maxN))
print("%-15s %15d" % (title7, minN))
