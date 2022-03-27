import bisect
import random


def prepare_data(n):
    number_list = []
    for i in range(n):
        number = random.randint(1, 10 * n)
        number_list.append(i)
    number_list.sort()
    return number_list


def find_number(n, number_list):
    index = 0
    for number in number_list:
        if number == n:
            return index
        index += 1
    return None


def find_number_with_lib_bisect(n, number_list):
    i = bisect.bisect_left(number_list, n)
    if i != len(number_list) and number_list[i] == n:
        return i
    return False


def find_number_bisect(n, number_list):
    start_index = 0
    end_index = len(number_list) - 1

    while start_index <= end_index:
        middle_index = (end_index + start_index) // 2
        if number_list[middle_index] == n:
            return middle_index
        elif n > number_list[middle_index]:
            start_index = middle_index + 1
        else:
            end_index = middle_index - 1
    return False
