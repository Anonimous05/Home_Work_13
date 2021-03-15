from random import randint


def random_list() -> list:
    arr = []
    for i in range(1, 10000000, 5):
        arr.append(i+randint(1, 4))

    return arr


mass = random_list()


def binarySearch(list, found, lower, higher):
    if lower > higher:
        return False
    else:
        center = (lower+higher) // 2
        if found == list[center]:
            return center
        elif found < list[center]:
            return binarySearch(list, found, lower, higher-1)
        else:
            return binarySearch(list, found, center+1, higher)


found = mass[len(mass)-150]

otvet = binarySearch(mass, found, 0, len(mass))

if otvet == False:
    print(f"Item {found} not found")
else:
    print(f"Item {found} found at index {otvet}")