import random
import sympy
import sys
from typing import List
from math import gcd


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

    p = int(input(f'Enter p(prime{", > " + str(len(text)) if operation == 1 else ""}): '))
    g = int(input(f'Enter 0 < g < {p}: '))
    x = int(input(f'Enter 0 < x < {p}: '))

    phi: int = p-1

    if operation == 1:

        m_i = digitization(text)

        '''k1: int = sympy.randprime(3, phi)
        k2: int = sympy.randprime(3, k1)
        k3: int = sympy.randprime(k1, phi)'''
        k1, k2, k3 = 3, 7, 13
        y = (g ** x) % p
        result_text = []
        choose_ai = 0
        for i in range(len(m_i)):

            # choose_ai = random.randint(1, 3)
            choose_ai += 1
            if choose_ai % 3 == 1:
                a, b = (g ** k1) % p, ((y ** k1) * m_i[i]) % p
                result_text.extend([a, b])

            if choose_ai % 3 == 2:
                a, b = (g ** k2) % p, ((y ** k2) * m_i[i]) % p
                result_text.extend([a, b])

            if choose_ai % 3 == 0:
                a, b = (g ** k3) % p, ((y ** k3) * m_i[i]) % p
                result_text.extend([a, b])

        print("Encrypted text: ", end='')
        for i in result_text: print(i, "", end="")

    if operation == 2:

        ab_list: List[int] = text.split()
        pairs = [int(i) for i in ab_list]

        result = ""

        for i in range(0, len(pairs) - 1, 2):
            result += alphabet[comparisons(pairs[i] ** x, pairs[i+1], p) - 1]

        answer = decryption_format(result)

        print("Decrypted text: ", end=' ')
        for i in answer: print(i, end='')


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

        print("Encrypted text: ", end='')
        for i in ciphertext: print(i, "", end='')

    if operation == 2:

        text: List[int] = text.split()
        result_text = ""

        for i in text: result_text += alphabet[((int(i) ** d) % n) - 1]

        answer = decryption_format(result_text)
        print("Decrypted text: ", end=' ')
        for i in answer: print(i, end='')


def euler_func(num):
    amount = 0
    for k in range(1, num + 1):
        if gcd(num, k) == 1:
            amount += 1
    return amount


def composition(point, k, a, p):

    ans_point = point
    delta = (((3 * point[0] ** 2 + a) % p) / ((2 * point[1]) % p)) % p

    if delta % 1 != 0:
        delta = ((3 * (ans_point[0]**2) + a) % p) * ((((2 * ans_point[1]) % p) ** (euler_func(p)-1)) % p) % p

    x = (delta ** 2 - 2 * ans_point[0]) % p
    y = (delta * (ans_point[0] - x) - ans_point[1]) % p
    ans_point = [int(x), int(y)]

    if k > 2:
        x_q = int(point[0])
        y_q = int(point[1])
        for i in range(k-2):
            if ans_point == "O":
                ans_point = point
                continue
            x_p = int(ans_point[0])
            y_p = int(ans_point[1])
            if point == ans_point:
                try:
                    delta = (3 * (x_p**2) + a) % p / (2 * y_p) % p
                    if delta % 1 != 0:
                        delta = ((3 * (x_p**2) + a) % p) * ((((2 * y_p) % p) ** (euler_func(p)-1)) % p) % p
                except ZeroDivisionError:
                    ans_point = "O"
                    continue
            else:
                if y_p == -y_q or -y_p == y_q:
                    ans_point = "O"
                    continue
                else:
                    try:
                        delta = (((y_q - y_p) % p)/((x_q - x_p) % p)) % p
                        if delta % 1 != 0:
                            delta = (((y_q - y_p) % p) * (((x_q - x_p) % p) ** (euler_func(p) - 1)) % p)
                    except ZeroDivisionError:
                        ans_point = "O"
                        continue

            x_r = (delta ** 2 - x_p - x_q) % p
            y_r = (((delta * (x_p - x_r)) % p) - y_p) % p
            ans_point = [int(x_r), int(y_r)]

    if type(ans_point) is list:
        return [ans_point[0], ans_point[1]]
    else:
        return False


def ECC(operation, text):

    '''
    a = int(input(" - Enter a: "))
    p_m = int(input(" - Enter p: "))
    c_b = int(input(" - Enter Cb: "))
    '''

    a, p_m, g, c_b, k, = 1, 11, [6, 5], 5, 4

    if operation == 1:
        '''
        g = list(map(int, input(" - Enter G: ").split()))
        k = int(input(" - Enter k: "))
        '''

        d_b = composition(g, c_b, a, p_m)
        r = composition(g, k, a, p_m)
        p = composition(d_b, k, a, p_m)

        print("Encrypted text: ", "(", r[0], ", ", r[1], ") ", ((int(text) * p[0]) % p_m), sep='', end='')

    if operation == 2:

        r = list(map(int, input(" - Enter R: ").split()))
        q = composition(r, c_b, a, p_m)
        x = q[0] ** (p_m - 2)

        print("Decrypted text: ", ((int(text) * x) % p_m))


while True:

    print("""Select a cipher: 
             1.  RSA
             2.  ElGamal
             3.  EСС
             4.  Exit
         """)
    select: int = int(input())
    if select == 4:
        sys.exit()

    if select not in [1, 2, 3, 4]:
        print("Wrong select!")
        continue

    print(""" Select an action: 
                1. Encryption 
                2. Decryption""")
    operation: int = int(input())
    if operation not in [1, 2]:
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

    if select == 3:
        ECC(operation, text)
        print()