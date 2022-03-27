import random


def prepare_random_data(n):
    number_list = []
    for i in range(n):
        number = random.randint(1, 10 * n)
        number_list.append(number)
    return number_list


def bubble_sort(list_of_numbers):
    number_of_elements = len(list_of_numbers)
    for i in range(number_of_elements - 1):
        for j in range(number_of_elements - 1):
            if list_of_numbers[j] > list_of_numbers[j + 1]:
                temp = list_of_numbers[j]
                list_of_numbers[j] = list_of_numbers[j + 1]
                list_of_numbers[j + 1] = temp
