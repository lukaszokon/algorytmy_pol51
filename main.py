import bisect
import datetime
import random

import wyszukiwanie, sortowanie


if __name__ == '__main__':

    DATA_SIZE = 10
    NUMBER_OF_TEST = 100

    sorted_list, unsorted_list, sorted_reversed_list, almost_sorted_list = sortowanie.prepare_number_lists(DATA_SIZE)
    print(sorted_list)
    print(unsorted_list)
    print(sorted_reversed_list)
    print(almost_sorted_list)
    # sortowanie.binary_sort(data)
    # print(data)

    '''
    DATA_SIZE = 800000
    NUMBER_OF_TEST = 100

    data = wyszukiwanie.prepare_data(DATA_SIZE)

    pomiary = []
    for i in range(NUMBER_OF_TEST):
        start_time = datetime.datetime.now()
        wyszukiwanie.find_number_with_lib_bisect(random.randint(1, DATA_SIZE * 10), data)
        end_time = datetime.datetime.now()
        pomiary.append(end_time - start_time)
    suma = datetime.timedelta()
    for pomiar in pomiary:
        suma = suma + pomiar
    suma = suma / NUMBER_OF_TEST
    print(suma)
    '''

