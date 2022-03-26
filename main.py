import rekurencja, sys


if __name__ == '__main__':
    sys.setrecursionlimit(100000)
    print(rekurencja.factorial_iter(3000))