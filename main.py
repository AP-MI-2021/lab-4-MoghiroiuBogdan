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


def cmmdc(l):
    '''
    cmmdc unor nr din lista
    :param l: lista de nr intregi
    :return: cmmdc
    '''
    cop = l[0]
    cop1 = l[1]
    while cop != cop1:
        if cop > cop1:
            cop = cop - cop1
        else:
            cop1 = cop1 - cop
    cm=cop
    for i in range(2,len(l)-1):
        x=l[i]
        while cm != x:
            if cm > x:
                cm=cm-x
            else:
                x=x-cm
        cm = x
    return cm


def test1():
    assert cmmdc([12,24,144]) == 12

def oglindit(x):
    '''
    afis oglinditul uni nr
    :param x: nr intreg
    :return: oglinditul numarului
    '''
    ogl=0
    while x != 0:
        ogl=ogl*10 + x%10
        x=x//10
    return ogl


def list_cmmdc(l):
    '''
    Afișarea listei obținute din lista inițială în care numerele pozitive și nenule au fost înlocuite cu
CMMDC-ul lor și numerele negative au cifrele în ordine inversă.
    :param l:lista de nr intregi
    :return:lista obținute din lista inițială în care numerele pozitive și nenule au fost înlocuite cu
CMMDC-ul lor și numerele negative au cifrele în ordine inversă.
    '''
    rez1 = []
    rez2 = []
    for x in l:
        if x > 0:
            rez1.append(x)
    cm = cmmdc(rez1)

    for x in l:
        if x > 0:
            rez2.append(cm)
        elif x < 0:
            x=x*(-1)
            ogl = 0
            while x != 0:
                ogl = ogl * 10 + x % 10
                x = x // 10
            ogl=ogl * (-1)
            rez2.append(ogl)

    return rez2


def test_list_cmmdc():
    assert list_cmmdc([-76, 12, 24, -13, 144]) == [-67, 12, 12, -31, 12]


def main():
    l = []
    test_nr_negative()
    test_nr_negative()
    test()
    test_list_superprim()
    test1()
    test_list_cmmdc()
    while True:
        print("1.citire lista")
        print("2.afiseaza nr negative din lista, nenule")
        print("3.Afișeaza cel mai mic număr care are ultima cifră egală cu o cifră citită de la tastatură")
        print("4.Afișarea tuturor numerelor din listă care sunt superprime.")
        print("5.Afișarea listei obținute din lista inițială în care numerele pozitive [...]")
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
        elif option == "5":
            print(list_cmmdc(l))
        elif option == "x":
            break
        else:
            print("optiune gresita!")


if __name__ == '__main__':
    main()