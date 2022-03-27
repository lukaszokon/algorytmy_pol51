import random


def prepare_data(n):
    number_list = []
    for i in range(n):
        number = random.randint(1, 10 * n)
        number_list.append(number)
    number_list.sort()
    return number_list


def find_number(n, number_list):
    index = 0
    for number in number_list:
        if number == n:
            return index
        index += 1
    return None
