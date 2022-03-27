import datetime
import random

import wyszukiwanie


if __name__ == '__main__':
    DATA_SIZE = 1000
    NUMBER_OF_TEST = 10

    data = wyszukiwanie.prepare_data(DATA_SIZE)

    pomiary = []
    for i in range(NUMBER_OF_TEST):
        start_time = datetime.datetime.now()
        wyszukiwanie.find_number(random.randint(1, DATA_SIZE * 10), data)
        end_time = datetime.datetime.now()
        pomiary.append(end_time - start_time)
    suma = datetime.timedelta()
    for pomiar in pomiary:
        suma = suma + pomiar
    suma = suma / NUMBER_OF_TEST
    print(suma)
