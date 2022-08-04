def dekor(funkcja):
    def wew():
        print("Masz do wyboru następujące funkcje matematyczne w naszym kalkulatorze:")
        return funkcja()

    return wew


def input_operation(min, max):
    operation = input("Którą opcję wybirasz?: ")
    if operation.isdigit() and int(operation) in list(range(min, max)):
        return int(operation)
    else:
        print("Wybierz jedną z właściwych wartości!")
        input_operation(min, max)


def input_value(pos):
    wartosc = input("Podaj %s wartość: " % pos)
    if wartosc.isdigit():
        return float(wartosc)
    else:
        print("Wpisana wartość musi byc liczbą!!")
        input_value(pos)


def exit_program():
    print("Koniec programu")
    exit()


def addFunction(pierwsza, druga):
    print("Wynik dodawania: {} + {} = {}\n".format(pierwsza, druga, pierwsza + druga))
    main()


def delFunction(pierwsza, druga):
    print("Wynik odejmowania: {} - {} = {}\n".format(pierwsza, druga, pierwsza - druga))
    main()


def mulFunction(pierwsza, druga):
    print("Wynik mnożenia: {} * {} = {}\n".format(pierwsza, druga, pierwsza * druga))
    main()


def divFunction(pierwsza, druga):
    if druga == 0:
        print("Nie można dzielić przez 0!!!\n")
    else:
        print("Wynik dzielenia: {} / {} = {}\n".format(pierwsza, druga, pierwsza / druga))
    main()


def expFunction(pierwsza, druga):
    print("Wynik potęgowania: {} ^ {} = {}\n".format(pierwsza, druga, pierwsza ** druga))
    main()


def sqrtFunction(pierwsza, druga):
    print("Wynik pierwiastkowania: {} sqrt {} = {}\n".format(druga, pierwsza, pierwsza ** (1 / druga)))
    main()


@dekor
def main():
    operMap = {1: "addFunction", 2: "delFunction", 3: "mulFunction", 4: "divFunction", 5: "expFunction",
               6: "sqrtFunction"}
    print("\n"
          "1 - dodawanie\n"
          "2 - odejmowanie\n"
          "3 - mnożenie\n"
          "4 - dzielenie\n"
          "5 - potęgowanie\n"
          "6 - pierwiastek\n"
          "\n"
          "0 - wyjście"
          "\n")

    position = input_operation(0, 7)
    if position in range(1, 8):
        action = operMap.get(int(position))
        pierwsza = input_value("pierwszą")
        druga = input_value("drugą")
        eval(action + '(%s, %s)' % (pierwsza, druga))
    elif position == 0:
        exit_program()
    else:
        print("Wprowadzona wartość jest niepoprawna.\n")
        main()


if __name__ == '__main__':
    main()
