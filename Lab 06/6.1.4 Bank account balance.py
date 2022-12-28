##
# this function calculates the balance of a bank account
# at the end of a time period
# accounting for an annual interest rate

def interestRate(balance, time, rate):
    trueRate = rate / 100
    for ys in range(time):
        balance *= (1 + trueRate)
    return balance

if __name__ == '__main__':
    initialBalance = float(input('> Initial balance [Lire italiane del 1936]= '))
    years = int(input('> Time [years] = '))
    interest = float(input('> Annual interest rate [%]= '))
    print(f'\nFinal balance = {interestRate(initialBalance, years, interest)}')
