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


def bubble_sort_1(list_of_numbers):  # 4n^2 - 8n + 5 -> O(n^2)
    number_of_elements = len(list_of_numbers)  # 1
    for i in range(number_of_elements - 1):  # n - 1, (n - 1) * (4n - 4) = 4n^2 - 4n - 4n +4= 4n^2 - 8n + 4
        for j in range(number_of_elements - 1):  # n - 1, (n - 1) * 4 = 4n - 4
            if list_of_numbers[j] > list_of_numbers[j + 1]:  # 1 , 4 * 1 = 4
                temp = list_of_numbers[j]  # 1
                list_of_numbers[j] = list_of_numbers[j + 1]  # 1
                list_of_numbers[j + 1] = temp  # 1


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
                if list_of_numbers[j] < list_of_numbers[j - 1]:
                    list_of_numbers[j], list_of_numbers[j - 1] = list_of_numbers[j - 1], list_of_numbers[j]
                else:
                    break


def merge_sort_piotr(list_of_numbers):
    # TODO Dziel na mniejsze listy z wykorzystaniem rekurencji

    if len(list_of_numbers) > 1:
        center = len(list_of_numbers) // 2
        left_section = list_of_numbers[:center]
        right_section = list_of_numbers[center:]

        merge_sort(left_section)
        merge_sort(right_section)

        a = 0
        b = 0
        c = 0
        # TODO Porównaj listy i scal
        while a < len(left_section) and b < len(right_section):
            if left_section[a] < right_section[b]:
                list_of_numbers[c] = left_section[a]
                a += 1
            else:
                list_of_numbers[c] = right_section[b]
                b += 1
            c += 1


def merge_sort_inner(start_index, end_index, list_of_numbers, temp_list):
    middle_index = (start_index + end_index + 1) // 2
    if middle_index - 1 - start_index > 0:
        merge_sort_inner(start_index, middle_index - 1, list_of_numbers, temp_list)
    if end_index - middle_index > 0:
        merge_sort_inner(middle_index, end_index, list_of_numbers, temp_list)

    # list_of_number jest podzielony na 2 części od start_index do middle - 1 i od middle do end_indexu
    # lewa część listy zaczyna się od start_indexu
    first_iterator = start_index
    # prawa część listy zaczyna się od middle_indexu
    second_iterator = middle_index

    # scalamy obie listy przy pomocy listy temp od startowego do end indexu
    for i in range(start_index, end_index + 1):
        # sprawdzamy, która liczba pomiędzy elementem wskazywanym przez first_iterator a elementem wskazywanym przez second
        # jest mniejszy ten jest dodawany do temp listy i odpowiadający iterator jest inkrementowany
        if (first_iterator == middle_index) or \
                (second_iterator <= end_index and list_of_numbers[first_iterator] > list_of_numbers[second_iterator]):
            temp_list[i] = list_of_numbers[second_iterator]
            second_iterator += 1
        else:
            temp_list[i] = list_of_numbers[first_iterator]
            first_iterator += 1

    for i in range(start_index, end_index + 1):
        list_of_numbers[i] = temp_list[i]


def merge_sort(list_of_numbers):
    start_index = 0
    end_index = len(list_of_numbers) - 1
    temp_list = [None] * len(list_of_numbers)
    merge_sort_inner(start_index, end_index, list_of_numbers, temp_list)


def selection_sort(list_of_numbers):
    n = len(list_of_numbers)
    for i in range(n - 1):
        min_value = list_of_numbers[i]
        min_index = i
        for j in range(i + 1, n):
            if list_of_numbers[j] < min_value:
                min_value = list_of_numbers[j]
                min_index = j
        list_of_numbers[i], list_of_numbers[min_index] = list_of_numbers[min_index], list_of_numbers[i]


def quick_sort(list_of_numbers):
    n = len(list_of_numbers)
    quick_sort_inner(list_of_numbers, 0, n - 1)


def quick_sort_inner(list_of_numbers, start_index, end_index):
    if start_index < end_index:
        pivot = list_of_numbers[start_index]
        pivot_index = start_index
        iterator = end_index
        while pivot_index != iterator:
            if iterator < pivot_index:
                if pivot < list_of_numbers[iterator]:
                    list_of_numbers[iterator], list_of_numbers[pivot_index] = list_of_numbers[pivot_index], list_of_numbers[
                        iterator]
                    pivot_index, iterator = iterator, pivot_index
                    continue
                iterator += 1
            else:
                if pivot > list_of_numbers[iterator]:
                    list_of_numbers[iterator], list_of_numbers[pivot_index] = list_of_numbers[pivot_index], list_of_numbers[
                        iterator]
                    pivot_index, iterator = iterator, pivot_index
                    continue
                iterator -= 1

        quick_sort_inner(list_of_numbers, start_index, pivot_index - 1)
        quick_sort_inner(list_of_numbers, pivot_index + 1, end_index)
