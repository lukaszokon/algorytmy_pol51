import random


def prepare_number_lists(n):
    unsorted_list = []
    for i in range(n):
        number = random.randint(1, 10 * n)
        unsorted_list.append(number)
    sorted_list = sorted(unsorted_list)
    sorted_reversed_list = sorted_list[::-1]
    almost_sorted_list = sorted_list
    middle = n//2
    almost_sorted_list[middle], almost_sorted_list[middle-1] = almost_sorted_list[middle-1], almost_sorted_list[middle]
    return sorted_list, unsorted_list, sorted_reversed_list, almost_sorted_list


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


def binary_sort(list):
    print(list)
    lenght = len(list)
    start_index = 0
    for i in range(1, len(list)):
        index = start_index
        was_change = False # zakończy operacje gdy juz wszystko jest na swoim miejscu
        while index + 1 < lenght:
            if list[index] > list[index+1]:
                a = list[index]
                b = list[index+1]
                list[index] = b
                list[index + 1] = a
                print(f'{a} to {list[index]}')
                if not was_change:
                    if index > 0:
                        start_index = index -1
                was_change =True
            else:
                print('ok')

            index += 1
        if not was_change: # jeśli wszytko jest na swoim miejscu to zakończy
            break
        lenght -= 1 #po każdej pętli największy element jest na końcu więc go pomijamy
        print(list)

    return list