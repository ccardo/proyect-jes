##
# removes noise from a generated list, averaging the values systematically,
# without creating another list
def main():
    import random
    integers = [float(random.randint(1, 100)) for _ in range(10)]
    print(integers)
    length = len(integers)
    for idx, num in enumerate(integers):
        if 0 < idx < length - 1:
            average = round((num + integers[idx-1] + integers[idx+1]) / 3, 2)
            integers.append(average)
        elif idx == 0:
            average = round((num + integers[idx+1]) / 2, 2)
            integers.append(average)
        elif idx == length - 1:
            average = round((num + integers[idx-1]) / 2, 2)
            integers.append(average)
        if idx >= length:
            integers = integers[length:]
            break
    print(f'smoothened out list = {integers}')

main()
