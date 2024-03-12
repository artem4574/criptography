from math import gcd


def euler_func(num):
    amount = 0
    for k in range(1, num + 1):
        if gcd(num, k) == 1:
            amount += 1
    return amount


def classic_euclid(num_1, num_2):
    while num_1 != 0 and num_2 != 0:
        if num_1 >= num_2:
            num_1 %= num_2
        else:
            num_2 %= num_1
    return num_1 or num_2

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def comparisons(a, b, m):
    print("Comparison: ", a, "X", " ≡ ", b, " (mod", m, ")", sep='')
    print("M % A = ")
    divider, divisible = m, a
    rem = divider % divisible
    n, arr_q, arr_rem = 0, [], []
    while rem != 0:
        integer = divider // divisible
        rem = divider % divisible
        arr_rem.append(rem)
        arr_q.append(integer)
        print(divider, "/", divisible, " = ", integer, "(", rem, ")", sep='')
        divider, divisible = divisible, rem
        n += 1
    if a % arr_rem[-2] != 0 or b % arr_rem[-2] != 0 or m % arr_rem[-2] != 0:
        print("Comparison have no solutions")
        return 0
    else:
        a /= arr_rem[-2]
        b /= arr_rem[-2]
        m /= arr_rem[-2]

        print("n     ", end='')
        for i in range(1, n+1): print(i, "  ", end='')
        print("\nq     ", end='')
        for i in arr_q: print(i, "  ", end='')
        print("\nP  1 ", arr_q[0], "  ", end='')
        p = [1, arr_q[0]]
        for i in range(2, n+1):
            p.append(arr_q[i-1]*p[i-1]+p[i-2])
            print(p[i], " ", end='')
        print("\nN =", n,
              "Pn-1 =", p[-2],
              "b =", int(b))
        print("X ≡ (-1)^", n-1, "*", p[-2], "*", int(b), "(mod", int(m), ")", " ≡ ", int(((-1)**(n-1) * p[-2] * b) % m), "(mod", int(m), ")", sep='')
        m *= arr_rem[-2]

        if arr_q[-2] != 1:
            print("X = ", end='')
            while m > m / arr_rem[-2]:
                print()
comparisons(3,1,77)


def hash(text, p):
    alphabet: str = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    tec_h = 0
    for i in range(len(text)):
        tec_h = ((tec_h + alphabet.index(text[i]) + 1) ** 2) % p
    return tec_h
print(hash('одиндуракможетбольшеспрашиватьзптчемдесятьумныхответяттчк',11))