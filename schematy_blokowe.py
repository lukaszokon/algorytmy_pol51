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
