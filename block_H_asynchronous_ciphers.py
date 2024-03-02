import random
import sympy
import sys
from typing import List


alphabet: str = "абвгдежзийклмнопрстуфхцчшщъыьэюя"


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


def eq(a: int, b: int, m: int):
    q: List[int] = euclid(a, m)
    if m < a: q.insert(0, 0)
    p: List = [1, q[0]]
    for i in range(1, len(q)): p.append(p[i] * q[i] + p[i-1])
    return ((-1)**(len(q) - 1) * p[-2] * b) % m


def digitization(open_text):
    result = []
    for i in range(len(open_text)): result.append(alphabet.index(open_text[i]) + 1)
    return result


def decryption_format(dec_text):
    dec_text = dec_text.replace('тчк', '.').replace('зпт', ',').replace('прб', ' ')
    result = dec_text[0].upper() + dec_text[1:]
    result_list = list(result)
    for i in range(len(result_list) - 3):
        if result_list[i] == ".":
            result_list[i + 2] = result_list[i + 2].upper()

    result = ""
    for char in result_list: result += char

    return result


def ElGamal(operation, text):

    p = int(input(f'Enter p(prime, > {len(text)}: '))
    g = int(input(f'Enter 0 < g < {p}: '))
    x = int(input(f'Enter 0 < x < {p}: '))

    m_i = digitization(text)
    phi: int = p-1

    if operation == 1:

        k1: int = sympy.randprime(3, phi)
        k2: int = sympy.randprime(3, k1)
        k3: int = sympy.randprime(k1, phi)
        # k1, k2, k3 = 3, 7, 13
        y = (g ** x) % p
        result_text = []
        # choose_ai = 0
        for i in range(len(m_i)):

            choose_ai = random.randint(1, 3)
            # choose_ai += 1
            if choose_ai % 3 == 1:
                a, b = (g ** k1) % p, ((y ** k1) * m_i[i]) % p
                result_text.extend([a, b])

            if choose_ai % 3 == 2:
                a, b = (g ** k2) % p, ((y ** k2) * m_i[i]) % p
                result_text.extend([a, b])

            if choose_ai % 3 == 0:
                a, b = (g ** k3) % p, ((y ** k3) * m_i[i]) % p
                result_text.extend([a, b])

        for i in result_text:
            print(i, "", end="")
        print()

    if operation == 2:
        ab: List[int] = [32, 33, 18, 10, 2, 23, 18, 7, 32, 5, 2, 36, 2, 7, 18, 6, 32, 34, 32, 18, 18, 26, 32, 1, 18, 21, 2, 9,
                         32, 5, 18, 8, 2, 35, 32, 11, 18, 31, 18, 23, 2, 31, 32, 5, 32, 12, 32, 1, 18, 20, 18, 30, 2, 35, 32,
                         3, 2, 5, 32, 21, 18, 12, 18, 28, 2, 7, 2, 33, 32, 29, 2, 19, 32, 16, 2, 5, 18, 24, 32, 11, 18, 28, 2,
                         19, 2, 36, 18, 33, 32, 15, 18, 9, 2, 25, 32, 16, 2, 36, 32, 5, 32, 25, 2, 7, 18, 28, 18, 12, 32, 18]

        pairs: List[List[int]] = [ab[i:i + 2] for i in range(0, len(ab), 2)]

        result: List[str] = []
        for pair in pairs:
            result.append(alphabet[eq(pair[0] ** x, pair[1], p) - 1])

        print(''.join(result))


def RSA(operation, text):

    p = int(input(" - Enter P(prime): "))
    q = int(input(" - Enter Q(another prime): "))
    n = p * q
    phi = (p-1) * (q-1)
    e = int(input(f" - Enter 1 < E < {phi}: "))
    d = eq(e, 1, phi)

    if operation == 1:

        digit_text = digitization(text)
        ciphertext = []

        for i in range(len(digit_text)): ciphertext.append((digit_text[i] ** e) % n)

        print("Encrypted text: ")
        for i in ciphertext: print(i, " ", end='')
        print()

    if operation == 2:

        text: List[int] = text.split()
        result_text = ""

        for i in text: result_text += alphabet[((int(i) ** d) % n) - 1]

        answer = decryption_format(result_text)
        print("Decrypted text: ", end=' ')
        for i in answer: print(i, end='')
        print()


while True:

    print("""Select a cipher: 
             1.  RSA
             2.  ElGamal
             3.  Exit
         """)
    select: int = int(input())
    if select == 3:
        sys.exit()

    if select not in [1, 2, 3]:
        print("Wrong select!")
        continue

    print(""" Select an action: 
                1. Encryption 
                2. Decryption""")
    operation: int = int(input())
    if operation not in [1, 2, 3]:
        print("Wrong select!")
        continue

    text: str = str(input('Enter text: '))
    print()

    if operation == 1:

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
