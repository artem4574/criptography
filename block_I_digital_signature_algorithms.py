from typing import List
import sys


def hash(text, p):
    alphabet: str = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    tec_h = 0
    for i in range(len(text)):
        tec_h = ((tec_h + alphabet.index(text[i]) + 1) ** 2) % p
    return int(tec_h)


def euclid(a: int, b: int):
    res: List[int] = []
    while a != 0 and b != 0:
        if a > b:
            res.append(a//b)
            a %= b
        else:
            res.append(b//a)
            b %= a
    return res


def eq(a: int, b: int, m: int) -> int:
    q: List[int] = euclid(a, m)
    if m < a: q.insert(0, 0)
    p: List = [1, q[0]]
    for i in range(1, len(q)): p.append(p[i] * q[i] + p[i-1])
    return ((-1)**(len(q) - 1) * p[-2] * b) % m


def comparisons(a, b, m):
    divider, divisible = m, a
    rem = divider % divisible
    n, arr_q, arr_rem = 0, [], []
    while rem != 0:
        integer = divider // divisible
        rem = divider % divisible
        arr_rem.append(rem)
        arr_q.append(integer)
        divider, divisible = divisible, rem
        n += 1
    if a % arr_rem[-2] != 0 or b % arr_rem[-2] != 0 or m % arr_rem[-2] != 0:
        print("Comparison have no solutions")
        return 0
    else:
        a /= arr_rem[-2]
        b /= arr_rem[-2]
        m /= arr_rem[-2]

        p = [1, arr_q[0]]
        for i in range(2, n+1):
            p.append(arr_q[i-1]*p[i-1]+p[i-2])
        return int(((-1)**(n-1) * p[-2] * b) % m)


def RSA(operation, text):

    p = int(input(" - Enter P(prime): "))
    q = int(input(" - Enter Q(another prime): "))
    n = p * q
    phi = (p - 1) * (q - 1)
    e = int(input(f" - Enter 1 < E < {phi}: "))
    # проверка на взаимную простоту
    d = eq(e, 1, phi)

    if operation == 1:

        s = (hash(text, n) ** d) % n
        print("Signature: ", s)

    if operation == 2:

        s = int(input(" - Enter S: "))

        if hash(text, n) == (s ** e) % n:
            print("The signature is approved!")
        else:
            print("Error in signature calculating")


def ElGamal(operation, text):

    p = int(input(" - Enter P(prime): "))
    g = int(input(f' - Enter G{"<" + str(p) if operation == 1 else ""}: '))
    x = int(input(f' - Enter X{"<" + str(p - 1) if operation == 1 else ""}: '))
    k = int(input(" - Enter K: "))  # k generation

    m = hash(text, p-1)
    y = (g ** x) % p

    if operation == 1:

        a = (g ** k) % p
        b = comparisons(k, m - x * a, p-1)

        print("Signature: (", a, ", ", b, ")", sep='')

    if operation == 2:

        s = list(map(int, input(" - Enter signature: ").split()))

        if ((y ** s[0]) * (s[0] ** s[1])) % p == (g ** m) % p:
            print("The signature is approved!")
        else:
            print("Error in signature!")


while True:

    print("""Select a DS algorithm: 
             1.  RSA
             2.  ElGamal
             3.  Exit
         """)
    select: int = int(input())
    if select == 4:
        sys.exit()

    if select not in [1, 2, 3]:
        print("Wrong select!")
        continue

    print(""" Select an action: 
                1. Signing 
                2. Сonfirmation
          """)
    operation: int = int(input())
    if operation not in [1, 2]:
        print("Wrong select!")
        continue

    text: str = str(input('Enter text: '))
    print()

    for i in range(len(text)):

        if text.find('.') != -1:
            index = text.find('.')
            str1_split1 = text[:index]
            str1_split2 = text[index + 1:]
            text = str1_split1 + 'тчк' + str1_split2

        if text.find(',') != -1:
            index = text.find(',')
            str1_split1 = text[:index]
            str1_split2 = text[index + 1:]
            text = str1_split1 + 'зпт' + str1_split2

        if text.find(' ') != -1:
            index = text.find(' ')
            str1_split1 = text[:index]
            str1_split2 = text[index + 1:]
            text = str1_split1 + 'прб' + str1_split2

    if select == 1:
        RSA(operation, text.lower())
        print()

    if select == 2:
        ElGamal(operation, text.lower())
        print()
