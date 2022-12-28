##
#   writing programs to generate certain lists after discovering the laws
#   used to make them (if they exist)

# I [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def i() -> list:
    return [i for i in range(1, 11)]


# II [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
def ii() -> list:
    return [i * 2 for i in range(11)]


# III [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
def iii() -> list:
    return [i ** 2 for i in range(1, 11)]


# IV [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
def iv() -> list:
    return [0] * 10


# V [1, 4, 9, 16, 9, 7, 4, 9, 11]
def v() -> list:
    return [1, 4, 9, 16, 9, 7, 4, 9, 11]


# VI [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
def vi() -> list:
    return [0 if i % 2 else 1 for i in range(1, 11)]


# VII [0, 1, 2, 3, 4, 0, 1, 2, 3, 4]
def vii() -> list:
    return [0, 1, 2, 3, 4] * 2
