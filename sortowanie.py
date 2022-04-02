import random
import timeit


def prepare_number_lists(n):
    unsorted_list = []
    for i in range(n):
        number = random.randint(1, 10 * n)
        unsorted_list.append(number)
    sorted_list = sorted(unsorted_list)
    sorted_reversed_list = sorted_list[::-1]
    almost_sorted_list = sorted_list.copy()
    middle = n // 2
    almost_sorted_list[middle], almost_sorted_list[middle - 1] = almost_sorted_list[middle - 1], almost_sorted_list[
        middle]
    return sorted_list, unsorted_list, sorted_reversed_list, almost_sorted_list


def test_sorting_function(sorting_function, data_number, number_of_tests):
    sorted_list, unsorted_list, sorted_reversed_list, almost_sorted_list = prepare_number_lists(data_number)
    test_code = f'sorting_function(list_to_sort)'
    print(timeit.timeit(stmt=test_code,
                        globals={'sorting_function': sorting_function,
                                 'list_to_sort': sorted_list},
                        number=number_of_tests))
    print(timeit.timeit(stmt=test_code,
                        globals={'sorting_function': sorting_function,
                                 'list_to_sort': unsorted_list},
                        number=number_of_tests))
    print(timeit.timeit(stmt=test_code,
                        globals={'sorting_function': sorting_function,
                                 'list_to_sort': sorted_reversed_list},
                        number=number_of_tests))
    print(timeit.timeit(stmt=test_code,
                        globals={'sorting_function': sorting_function,
                                 'list_to_sort': almost_sorted_list},
                        number=number_of_tests))


def bubble_sort_1(list_of_numbers):
    number_of_elements = len(list_of_numbers)
    for i in range(number_of_elements - 1):
        for j in range(number_of_elements - 1):
            if list_of_numbers[j] > list_of_numbers[j + 1]:
                temp = list_of_numbers[j]
                list_of_numbers[j] = list_of_numbers[j + 1]
                list_of_numbers[j + 1] = temp


def bubble_sort_2(list_of_numbers):
    number_of_elements = len(list_of_numbers)
    end_index = number_of_elements - 1
    for i in range(number_of_elements - 1):
        for j in range(end_index):
            if list_of_numbers[j] > list_of_numbers[j + 1]:
                temp = list_of_numbers[j]
                list_of_numbers[j] = list_of_numbers[j + 1]
                list_of_numbers[j + 1] = temp
        end_index -= 1


def bubble_sort_3(list_of_numbers):
    number_of_elements = len(list_of_numbers)
    end_index = number_of_elements - 1
    for i in range(number_of_elements - 1):
        was_change = False
        for j in range(end_index):
            if list_of_numbers[j] > list_of_numbers[j + 1]:
                temp = list_of_numbers[j]
                list_of_numbers[j] = list_of_numbers[j + 1]
                list_of_numbers[j + 1] = temp
                was_change = True
        if not was_change:
            break
        end_index -= 1


def bubble_sort_4(list_of_numbers):
    number_of_elements = len(list_of_numbers)
    end_index = number_of_elements - 1
    start_index = 0
    for i in range(number_of_elements - 1):
        was_change = False
        for j in range(start_index, end_index):
            if list_of_numbers[j] > list_of_numbers[j + 1]:
                temp = list_of_numbers[j]
                list_of_numbers[j] = list_of_numbers[j + 1]
                list_of_numbers[j + 1] = temp
                if not was_change:
                    if j > 0:
                        start_index = j - 1
                was_change = True
        if not was_change:
            break
        end_index -= 1


def insert_sort(list_of_numbers):
    for i in range(1, len(list_of_numbers)):
        for j in range(i, 0, -1):
            if j == 0:
                break
            else:
                if list_of_numbers[j] < list_of_numbers[j-1]:
                    list_of_numbers[j], list_of_numbers[j-1] = list_of_numbers[j-1], list_of_numbers[j]
                else:
                    break