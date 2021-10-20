def citire_lista():
    l = []
    givenString = input("dati lista:")
    numberAsString = givenString.split(",")

    for x in numberAsString:
        l.append(int(x))
    return l


def nr_negative(l):
    '''
    afiseaza nr negative din lista, nenule
    :param l: lista de nr intregi
    :return: nr negative din lista, nenule
    '''
    rez = []
    for x in l:
        if x < 0:
            rez.append(x)
    return rez


def test_nr_negative():
    assert  nr_negative([1,3,-43,0,-5]) == [-43,-5]


def nr_mic(l,k):
    '''
    Afișarea celui mai mic număr care are ultima cifră egală cu o cifră citită de la tastatură.
    :param l: lista de nr intregi
    :return: cel mai mic număr care are ultima cifră egală cu o cifră citită de la tastatură
    '''
    min = None
    for x in l:
        if x % 10 == k and (min is None or x < min):
            min = x
    return min


def test_nr_mic():
    assert nr_mic([1, 6, 34, 68, 40, 48, 20], 8) == 48


def is_superprime(n):
    '''
    Determină dacă un număr este superprim: dacă toate prefixele sale sunt prime.
    :param n: nr natural
    :return: true=este superprim sau false=NU este superprim
    '''
    p = 1
    cop = n
    while cop > 9:
        cop = cop // 10
        p = p * 10

    while p != 0:
        nr = n // p
        for i in range(2, nr // 2 + 1):
            if nr % i == 0:
                return False
        p = p // 10

    return True


def test():
    assert is_superprime(239) is True
    assert is_superprime(237) is False
    assert is_superprime(233) is True

def list_superprim(l):
    '''
    Afișarea tuturor numerelor din listă care sunt superprime.
    :param l: lista de nr intregi
    :return:toate numerelor din listă care sunt superprime.
    '''
    rezultat = []
    for x in l:
        if (x > 0) and is_superprime(x) is True:
            rezultat.append(x)
    return rezultat


def test_list_superprim():
    assert list_superprim([237,239,233]) == [239,233]



def main():
    l = []
    test_nr_negative()
    test_nr_negative()
    test()
    test_list_superprim()
    while True:
        print("1.citire lista")
        print("2.afiseaza nr negative din lista, nenule")
        print("3.Afișeaza cel mai mic număr care are ultima cifră egală cu o cifră citită de la tastatură")
        print("4.Afișarea tuturor numerelor din listă care sunt superprime.")
        print("x.IESIRE")
        option = input("dati nr=")

        if option == "1":
            l = citire_lista()
        elif option == "2":
            print(nr_negative(l))
        elif option == "3":
            k=int(input("dati k="))
            print(nr_mic(l,k))
        elif option == "4":
            print(list_superprim(l))
        elif option == "x":
            break
        else:
            print("optiune gresita!")


if __name__ == '__main__':
    main()