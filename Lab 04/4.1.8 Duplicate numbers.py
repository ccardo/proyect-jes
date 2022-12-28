##
# this code will detect any adjacent duplicate digits in a given integer
import definitions
numbers = definitions.input_one_character_at_a_time()
print(f'Your sequence is: {numbers}\n')  # lets the user read the number sequence in one string

# DUPLICATE CHECKER
# 'k' acts as a placeholder to keep track of the start of the duplicate sequence
if numbers.isdigit():
    k = 0
    for index in range(len(numbers) - 1):
        k = k + 1
        if numbers[index] == numbers[index + 1]:  # checks if the number is equal to the next in the string
            if index == 0:  # makes an exception for index == 0
                k = 0
            if numbers[index] not in numbers[index - k:index]:  # checks if the same number is not already
                # in the string after the placeholder - that would mean it's already part of the duplicate sequence
                print('duplicate number: ', numbers[index])
        else:
            k = 0  # resets the value of k to zero after the sequence has ended
