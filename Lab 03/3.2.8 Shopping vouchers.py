##
expense = float(input("how much have you spent on food? "))
voucher = 8

if expense < 10:
    print("you don't have the right to any voucher")
    exit("sorry poveraccio del cazzo :(")
elif 10 <= expense <= 60:
    voucher = 0.08 * expense

elif 60 < expense <= 150:
    voucher = 0.1 * expense

elif 150 < expense <= 210:
    voucher = 0.12 * expense

else:
    voucher = 0.14 * expense

print("you have the right to a", round(voucher), "dollar discount voucher on your", expense, "dollar expense :)")
