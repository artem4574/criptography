import random
import sys
from math import gcd


def hash_quad(text, p):
    alphabet: str = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    tec_h = 0
    for i in range(len(text)):
        tec_h = ((tec_h + alphabet.index(text[i]) + 1) ** 2) % p
    return int(tec_h)


def euler_func(num):
    amount = 0
    for k in range(1, num + 1):
        if gcd(num, k) == 1:
            amount += 1
    return amount


def is_prime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d ** 2 <= n and n % d != 0:
        d += 2
    return d ** 2 > n


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
        for _ in range(k - 2):
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


def point_addition(point_1: list, point_2: list, a, p):

    x_q, y_q = int(point_1[0]), int(point_1[1])
    x_p, y_p = int(point_2[0]), int(point_2[1])

    if point_1 == point_2:
        try:
            delta = (3 * (x_p ** 2) + a) % p / (2 * y_p) % p
            if delta % 1 != 0:
                delta = ((3 * (x_p ** 2) + a) % p) * ((((2 * y_p) % p) ** (euler_func(p) - 1)) % p) % p
        except ZeroDivisionError:
            return False
    else:
        if y_p == -y_q or -y_p == y_q:
            return False
        else:
            try:
                delta = (((y_q - y_p) % p) / ((x_q - x_p) % p)) % p
                if delta % 1 != 0:
                    delta = (((y_q - y_p) % p) * (((x_q - x_p) % p) ** (euler_func(p) - 1)) % p)
            except ZeroDivisionError:
                return False

    x_r = (delta ** 2 - x_p - x_q) % p
    y_r = (((delta * (x_p - x_r)) % p) - y_p) % p

    return [int(x_r), int(y_r)]


def GOSTR_34_10_94(operation, text):

    p = int(input(" - Enter P(prime): "))
    if not is_prime(p):
        print("P should be prime!")
        exit()
    q = int(input(f" - Enter Q(prime multiplier of {p-1}): "))
    if not is_prime(q) or (p - 1) % q != 0:
        print(f"Q should be prime multiplier of {p-1}!")
        exit()
    a = int(input(f" - Enter A(1 < A < {p - 1}, a ^ q mod p = 1): "))
    if a >= p-1 or a**q % p != 1:
        print(f"a should be < {p-1} and a ^ q mod p = 1")
        exit()

    m = hash_quad(text, q) if hash_quad(text, q) != 0 else 1

    if operation == 1:
        r, s = 0, 0

        x = int(input(f" - Enter X( < {q}): "))
        if x >= q:
            print(f"X >= Q")
            exit()

        y = (a ** x) % p

        while r <= 0:
            k: int = random.randint(1, q - 1)
            r = ((a ** k) % p) % q
            s = (x * r + k * hash_quad(text, q)) % q
        print("Y =", y)
        print("Signature: ", r % (2 ** 256), s % (2 ** 256))

    if operation == 2:

        s = list(map(int, input(" - Enter signature: ").split()))
        y = int(input(" - Enter Y: "))

        v = m ** (q - 2) % q
        z_1 = (s[1] * v) % q
        z_2 = ((q - s[0]) * v) % q
        u = (((a ** z_1) * (y ** z_2)) % p) % q

        if u == s[0]:
            print("The signature is approved!")
        else:
            print("Error in signature!")


def GOSTR_34_10_2012(operation, text):

    a = int(input(" - Enter a: "))
    p_m = int(input(" - Enter p: "))
    if not is_prime(p_m):
        print("P should be prime!")
        exit()
    g = list(map(int, input(" - Enter G: ").split()))

    q = 1
    while composition(g, q, a, p_m):
        q += 1
    # q = int(input(" - Enter q: "))
    m = hash_quad(text, p_m)

    if operation == 1:

        r, s = 0, 0

        x_a: int = random.randint(1, q - 1)
        # x_a = int(input(" - Enter x_a: "))
        y_a = composition([g[0], g[1]], x_a, a, p_m)

        while r <= 0 and s <= 0:
            k: int = random.randint(1, q - 1)
            # k = int(input(" - Enter k: "))
            p = composition([g[0], g[1]], k, a, p_m)
            r = p[0] % q
            s = ((k * m) + (r * x_a)) % q

        print("Signature: ", r, s)
        print("Y:", y_a)

    if operation == 2:

        s = list(map(int, input(" - Enter signature: ").split()))
        y_a = list(map(int, input(" - Enter Y: ").split()))

        if s[0] > 0 and s[1] < q:
            u_1 = s[1] * (m ** (q - 2))
            u_2 = -s[0] * (m ** (q - 2))
            p = point_addition(composition(g, u_1, a, p_m), composition(y_a, u_2, a, p_m), a, p_m)
            if p and p[0] % q == s[0]:
                print("The signature is approved!")
            else:
                print("Error in signature!")
        else:
            print("Error in signature!")


while True:

    print("""Select a DS algorithm: 
             1.  GOST R 34.10-94
             2.  GOST R 34.10-2012
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
        GOSTR_34_10_94(operation, text.lower())
        print()

    if select == 2:
        GOSTR_34_10_2012(operation, text.lower())
        print()

