##
#

def flood_map(heights, waterLevel):

    for row in heights:
        for col in row:
            print("*", end=' ') if col < waterLevel else print(" ", end=' ')
        print()


