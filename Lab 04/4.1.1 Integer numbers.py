# 04.1.1 integer numbers
done = False
somma = 0
even = 0
odd = 0
integer = int(input('Insert an integer number: '))
maximum = integer - 1
minimum = integer

while not done:

    somma = somma + integer
    print(f'\nthe partial sum is: {somma}')

    if integer // 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
    print(f'there are a total of {even} even numbers, and {odd} odd numbers')

    if integer < minimum:
        minimum = integer
    elif integer >= maximum:
        maximum = integer
    print(f'the maximum of the partial sequence is {maximum}, the minimum is {minimum}')

    integerInput = input('Insert another integer number: ')
    integer = int(integerInput)

    if integerInput.upper() == 'DONE':
        done = True

exit('you have exited the program')
