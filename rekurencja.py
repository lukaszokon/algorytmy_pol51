def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def factorial_iter(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorial_dynamic(n, memory={0:1, 1:1}):
    if n in memory:
        return memory[n]
    else:
        memory[n] = n * factorial_dynamic(n-1)
    return memory[n]


def fib_dynamic(n, memory={0:0, 1:1, 2:1}):
    if n in memory:
        return memory[n]
    else:
        memory[n] = fib_dynamic(n - 2) + fib_dynamic(n - 1)
        return memory[n]


def fib_iter(n):
    a = 0
    b = 1

    for i in range(n-1):
        temp = b
        b = b + a
        a = temp
    return b