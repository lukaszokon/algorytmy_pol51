from math import sqrt


def is_prime(n):
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


def generate_prime(n):
    primes = 0
    number_to_check = 2
    primes_list = []
    while primes < n:
        if is_prime(number_to_check):
            primes_list.append(number_to_check)
            primes += 1
        number_to_check += 1
    return primes_list