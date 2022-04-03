import bisect
import datetime
import random

import wyszukiwanie, sortowanie, struktury_danych

def test_sort_for_10_numbers(sort_function):
    DATA_SIZE = 10
    sorted_list, unsorted_list, sorted_reversed_list, almost_sorted_list = sortowanie.prepare_number_lists(DATA_SIZE)
    # print(sorted_list)
    # sort_function(sorted_list)
    # print(sorted_list)

    print(unsorted_list)
    sort_function(unsorted_list)
    print(unsorted_list)

    # print(sorted_reversed_list)
    # sort_function(sorted_reversed_list)
    # print(sorted_reversed_list)

    # print(almost_sorted_list)
    # sort_function(almost_sorted_list)
    # print(almost_sorted_list)


if __name__ == '__main__':
    stack = struktury_danych.Stack()

    for i in range(5):
        stack.push(i)

    for i in range(6):
        print(stack.pop())


















    # test_sort_for_10_numbers(sortowanie.quick_sort)


    # DATA_SIZE = 20000
    # NUMBER_OF_TEST = 10

    # print("bubble_sort_2")
    # sortowanie.test_sorting_function(sortowanie.bubble_sort_2, DATA_SIZE, NUMBER_OF_TEST)
    # print("bubble_sort_3")
    # sortowanie.test_sorting_function(sortowanie.bubble_sort_3, DATA_SIZE, NUMBER_OF_TEST)
    # print("bubble_sort_4")
    # sortowanie.test_sorting_function(sortowanie.bubble_sort_4, DATA_SIZE, NUMBER_OF_TEST)
    # print("insert_sort")
    # sortowanie.test_sorting_function(sortowanie.insert_sort, DATA_SIZE, NUMBER_OF_TEST)
    # print("merge_sort")
    # sortowanie.test_sorting_function(sortowanie.merge_sort, DATA_SIZE, NUMBER_OF_TEST)




