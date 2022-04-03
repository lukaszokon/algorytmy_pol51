import bisect
import datetime
import random
import sys

import wyszukiwanie, sortowanie, struktury_danych, liczby_pierwsze

def test_sort_for_10_numbers(sort_function):
    DATA_SIZE = 10
    sorted_list, unsorted_list, sorted_reversed_list, almost_sorted_list = sortowanie.prepare_number_lists(DATA_SIZE)
    print(sorted_list)
    sort_function(sorted_list)
    print(sorted_list)

    print(unsorted_list)
    sort_function(unsorted_list)
    print(unsorted_list)

    print(sorted_reversed_list)
    sort_function(sorted_reversed_list)
    print(sorted_reversed_list)

    print(almost_sorted_list)
    sort_function(almost_sorted_list)
    print(almost_sorted_list)


if __name__ == '__main__':


    print(liczby_pierwsze.generate_prime(100000))
    # stack = struktury_danych.Stack()
    #
    # for i in range(5):
    #     stack.push(i)
    #
    # for i in range(6):
    #     print(stack.pop())
    #
    # print()

    # my_list = struktury_danych.MyList()
    # for i in range(5):
    #     my_list.insert(i)

    # print(1 in my_list)

    # zmienna = mylist[2]
    # print(zmienna)

    # for i in range(6):
    #     print(my_list.delete())




    # test_sort_for_10_numbers(struktury_danych.heapsort)

    # sys.setrecursionlimit(999999999)
    DATA_SIZE = 1000
    NUMBER_OF_TEST = 100

    # print("bubble_sort_2")
    # sortowanie.test_sorting_function(sortowanie.bubble_sort_2, DATA_SIZE, NUMBER_OF_TEST)
    # print("bubble_sort_3")
    # sortowanie.test_sorting_function(sortowanie.bubble_sort_3, DATA_SIZE, NUMBER_OF_TEST)
    # print("bubble_sort_4")
    # sortowanie.test_sorting_function(sortowanie.bubble_sort_4, DATA_SIZE, NUMBER_OF_TEST)
    # print("insert_sort")
    # sortowanie.test_sorting_function(sortowanie.insert_sort, DATA_SIZE, NUMBER_OF_TEST)
    # print("quick_sort")
    # sortowanie.test_sorting_function(sortowanie.quick_sort, DATA_SIZE, NUMBER_OF_TEST)
    # print("merge_sort")
    # sortowanie.test_sorting_function(sortowanie.merge_sort, DATA_SIZE, NUMBER_OF_TEST)
    # print("heap_sort")
    # sortowanie.test_sorting_function(struktury_danych.heapsort, DATA_SIZE, NUMBER_OF_TEST)



