def pole_kwadratu():
    a = float(input("Podaj długość boku kwadratu: "))
    P = a * a
    return P


def wpisywanie_hasla():
    password = None
    while password != "854":
        password = input("Wpisz hasło: ")
    print("Kod zaakceptowany")
    return


def dec_to_bin():
    d = int(input("Wpisz liczbę całkowitą >=0: "))
    bin_str = ""
    while d != 0:
        r = d % 2
        if r == 1:
            bin_str = '1' + bin_str
        else:
            bin_str = '0' + bin_str
        d = d // 2
    print(bin_str)
    return
