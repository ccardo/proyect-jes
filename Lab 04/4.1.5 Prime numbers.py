##
# the code checks whether the given number is prime or not
# it does so by dividing by increasingly large numbers
# and checking if the quotient is an integer
number = int(input("Enter number: "))
divisor = 2

if number <= 1:
    print(f"{number} is not a prime number")
elif number == 2:
    print(f"{number} is a prime number")
else:
    while divisor <= number:
        R = number % divisor
        if R == 0 and divisor < number:
            print(f'{number} is not a prime number')
            print(f'{number} is divisible by {divisor}')
            break
        else:
            divisor = divisor + 1
            if R == 0 and divisor >= number:
                print(f'{number} is a prime number')
                break
