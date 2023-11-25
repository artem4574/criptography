import random
import sympy
import itertools
from typing import List

alphabet: str = "абвгдежзийклмнопрстуфхцчшщъыьэюя"

def euclid(a: int, b: int) -> List[int]:
    res: List[int] = []
    while a != 0 and b != 0:
        if a > b:
            res.append(a//b)
            a = a % b
        else:
            res.append(b//a)
            b = b % a
    return res


def eq(a: int, b: int, m: int) -> int:
    q: List[int] = euclid(a, m)
    if (m < a): q.insert(0, 0)
    P: List = [1, q[0]]
    for i in range(1, len(q)): P.append(P[i]*q[i]+P[i-1])
    return ((-1)**(len(q) - 1) * P[-2] * b) % m



def digitization(open_text, result = []):
    for i in range(len(open_text)): result.append(alphabet.index(open_text[i])+1)
    return result


P = int(input('Enter p(prime): '))
x = int(input('Enter x(0 < x < p): '))
g = int(input('Enter g(0 < g < p): '))

M_i = digitization("один дурак может больше спрашивать зпт чем десять умных ответить тчк".replace(' ', ''))
phi: int = P-1
'''k1: int = sympy.randprime(3, phi)
k2: int = sympy.randprime(3, k1)
k3: int = sympy.randprime(k1, phi)'''
k1 = 3
k2 = 7
k3 = 13


Y = (g**x) % P
#print("\n ", k1, k2, k3, Y)
result_text = []
choose_ai = 0
for i in range(len(M_i)):
    #choose_ai = random.randint(1,3)
    choose_ai +=1
    if choose_ai % 3 == 1:
        a = (g**k1) % P
        b = ((Y**k1)*M_i[i]) % P
        result_text.append(a)
        result_text.append(b)
    if choose_ai % 3 == 2:
        a = (g**k2) % P
        b = ((Y**k2)*M_i[i]) % P
        result_text.append(a)
        result_text.append(b)
    if choose_ai % 3 == 0:
        a = (g**k3) % P
        b = ((Y**k3)*M_i[i]) % P
        result_text.append(a)
        result_text.append(b)


'''for i in result_text:
    print(i, "", end="")'''

print()

P = 37
g = 20
x = 19
ab: List[int] = [32, 33, 18, 10, 2, 23, 18, 7, 32, 5, 2, 36, 2, 7, 18, 6, 32, 34, 32, 18, 18, 24, 32, 1, 18, 21, 2, 9,
                 32, 5, 18, 8, 2, 35, 32, 11, 18, 31, 18, 23, 2, 31, 32, 5, 32, 12, 32, 1, 18, 20, 18, 30, 2, 35, 32,
                 3, 2, 5, 32, 21, 18, 12, 18, 28, 2, 7, 2, 33, 32, 29, 2, 19, 32, 16, 2, 5, 18, 24, 32, 11, 18, 28, 2,
                 19, 2, 36, 18, 33, 32, 15, 18, 9, 2, 25, 32, 16, 2, 36, 32, 5, 32, 25, 2, 7, 18, 28, 18, 12, 32, 18]

pairs: List[List[int]] = [ab[i:i + 2] for i in range(0, len(ab), 2)]

result: List[str] = []
for pair in pairs:
    result.append(alphabet[eq(pair[0]**x, pair[1], P) - 1])

print (''.join(result))

