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


def is_prime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d ** 2 <= n and n % d != 0:
        d += 2
    return d ** 2 > n


def eq(a: int, b: int, m: int) -> int:
    q: List[int] = euclid(a, m)

    if m < a:
        q.insert(0, 0)
    p: List = [1, q[0]]

    for i in range(1, len(q)):
        p.append(p[i] * q[i] + p[i-1])

    return ((-1) ** (len(q) - 1) * p[-2] * b) % m


def euler_func(num):
    amount = 0
    for k in range(1, num + 1):
        if gcd(num, k) == 1:
            amount += 1
    return amount


def El_Gamal_key_generate(phi) -> int:
    key = 0
    while gcd(key, phi) != 1:
        key: int = sympy.randprime(3, phi)
    return key
        
        
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

        return int(((-1) ** (n-1) * p[-2] * b) % m)


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

    p = int(input(f'Enter p(prime{", > " + str(32) if operation == 1 else ""}): '))
    if not is_prime(p) or p < 32:
        print("P should be prime and > 32!")
        exit()
    g = int(input(f'Enter 0 < g < {p}: '))
    # x = int(input(f'Enter 0 < x < {p}: '))
    x = random.randint(2, p-1)
    if p <= x or p <= g or x <= 1 or g <= 1:
        print("1 < x < p and 1 < g < p!")
        exit()

    phi: int = p-1

    if operation == 1:

        m_i = digitization(text)
        
        y = (g ** x) % p
        result_text = []

########################_TEST_MODE_########################
        '''choose_key, k1, k2, k3 = 0, 3, 7, 13
        
        for i in range(len(m_i)):

            choose_key += 1
            if choose_key % 3 == 1:
                a, b = (g ** k1) % p, ((y ** k1) * m_i[i]) % p
                result_text.extend([a, b])

            if choose_key % 3 == 2:
                a, b = (g ** k2) % p, ((y ** k2) * m_i[i]) % p
                result_text.extend([a, b])

            if choose_key % 3 == 0:
                a, b = (g ** k3) % p, ((y ** k3) * m_i[i]) % p
                result_text.extend([a, b])'''

##########################################################

        for i in range(len(m_i)):

            key = El_Gamal_key_generate(phi)
            a, b = (g ** key) % p, ((y ** key) * m_i[i]) % p
            result_text.extend([a, b])

        print("X =", x, "Encrypted text: ", end='')
        for i in result_text: print(i, "", end="")

    if operation == 2:

        x = int(input("Enter X: "))

        ab_list: List[int] = text.split()
        pairs = [int(i) for i in ab_list]

        result = ""

        for i in range(0, len(pairs) - 1, 2):
            result += alphabet[comparisons(pairs[i] ** x, pairs[i+1], p) - 1]

        answer = decryption_format(result)

        print("Decrypted text: ", end=' ')
        for i in answer: print(i, end='')
        print()


def RSA(operation, text):

    if operation == 1:

        p = int(input(" - Enter P(prime): "))
        q = int(input(" - Enter Q(another prime): "))
        if not is_prime(p) or not is_prime(q):
            print("P and Q should be prime!")
            exit()
        n = p * q
        if n < 32:
            print("P * Q < 32!")
            exit()
        phi = (p - 1) * (q - 1)
        e = int(input(f" - Enter 1 < E < {phi}: ")) if len(text) < 1000 else phi

        while gcd(e, phi) != 1 or e >= phi or e <= 1:
            e: int = sympy.randprime(3, phi)

        digit_text = digitization(text)
        ciphertext = []

        for i in range(len(digit_text)):
            ciphertext.append((digit_text[i] ** e) % n)

        print("N = ", n, ", E = ", e, sep='')
        print("Encrypted text: ", end='')
        for i in ciphertext: print(i, "", end='')
        print()

    if operation == 2:
        n = int(input(" - Enter N: "))
        phi = euler_func(n)
        e = int(input(" - Enter E: "))
        d = eq(e, 1, phi)
        text: List[int] = text.split()
        result_text = ""

        for i in text:
            result_text += alphabet[((int(i) ** d) % n) - 1]

        answer = decryption_format(result_text)
        print("Decrypted text: ", end=' ')
        for i in answer: print(i, end='')


def ECC(operation, text):

    """
    a = int(input(" - Enter a: "))
    b = int(input(" - Enter b: "))
    p_m = int(input(" - Enter p: "))
    c_b = int(input(" - Enter Cb: "))

    q_m = 1
    while composition(g, q_m, a, p_m):
        q_m += 1
    """

    a, b, p_m, g, c_b, q_m = 1, 3, 41, [3, 22], 4, 39

    if operation == 1:

        ciphertext = []
        digit_text = digitization(text)

        for i in range(len(digit_text)):

            k = random.randint(2, q_m - 1)
            d_b = composition(g, c_b, a, p_m)
            r = composition(g, k, a, p_m)
            p = composition(d_b, k, a, p_m)

            ciphertext.extend([r[0], r[1], (digit_text[i] * p[0]) % p_m])

        print("Encrypted text: ", end='')
        for i in ciphertext: print(i, "", end='')

########################_TEST_MODE_########################
        """
        k = 4
        d_b = composition(g, c_b, a, p_m)
        r = composition(g, k, a, p_m)
        p = composition(d_b, k, a, p_m)
        print("Encrypted text: ", "(", r[0], ", ", r[1], ") ", ((int(text) * p[0]) % p_m), sep='', end='')
        """

###########################################################

    if operation == 2:

        text_list: List[int] = text.split()
        point_list = [int(i) for i in text_list]
        dec_text = ""

        for i in range(0, len(point_list) - 2, 3):

            r = [point_list[i], point_list[i+1]]
            q = composition(r, c_b, a, p_m)
            x = q[0] ** (p_m - 2)

            dec_text += alphabet[((point_list[i+2] * x) % p_m) - 1]

        answer = decryption_format(dec_text)
        print("Decrypted text: ", end=' ')
        for i in answer: print(i, end='')

########################_TEST_MODE_########################
        """
        r = list(map(int, input(" - Enter R: ").split()))
        q = composition(r, c_b, a, p_m)
        x = q[0] ** (p_m - 2)
        print("Decrypted text: ", ((int(text) * x) % p_m))
        """
###########################################################


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
        ECC(operation, text.lower())
        print()