from definitions import get_integer
##
# this function calculates data for the government
#


def economicSubsidy(income, children):
    if 30_000 <= income < 40_000 and children >= 3:
        return 1000 * children
    elif 20_000 <= income < 30_000 and children >= 2:
        return 1500 * children
    elif income < 20_000:
        return 2000 * children
    else:
        print("You don't satisfy the conditions required\n"
              "to access an economic subsidy from the government.")

if __name__ == "__main__":
    while 10 < 11:
        check = input('> Press ENTER to continue [type -1 to finish]')
        if check == '-1':
            exit()
        annualIncome = get_integer('> Annual income: ', "\n[Please enter an integer]")
        childNumber = get_integer('> Number of children: ', "'n [Please don't cut your son in half, enter an integer]")
        print(f'You have the right to an economic subsidy of: {economicSubsidy(annualIncome, childNumber)}\n')
