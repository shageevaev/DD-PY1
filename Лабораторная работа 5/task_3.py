import random


def get_unique_list_numbers() -> list[int]:
    myList = []
    for i in range(-10, 11):
        myList.append(i)

    for i in range(6):
        randDel = round(random.random()*(len(myList)-1))
        myList.pop(randDel)

    return myList


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))

