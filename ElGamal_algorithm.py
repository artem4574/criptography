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


P: int = int(input('Enter p(prime): '))
x: int = int(input('Enter x(0 < x < p): '))
g: int = int(input('Enter g(0 < g < p): '))

M_i = digitization("один дурак может больше спрашивать зпт чем десять умных ответить тчк".replace(' ', ''))
phi: int = P-1
k1: int = sympy.randprime(13, phi)
k2: int = sympy.randprime(0, k1)
k3: int = sympy.randprime(0, k2)
Y = (g**x) % P
result_text = []
for i in range(len(M_i)):
    choose_ai = random.randint(1,3)
    if choose_ai == 1:
        a = (g**k1) % P
        b = ((Y**k1)*M_i[i]) % P
        result_text.append(a)
        result_text.append(b)
    if choose_ai == 2:
        a = (g**k2) % P
        b = ((Y**k2)*M_i[i]) % P
        result_text.append(a)
        result_text.append(b)
    if choose_ai == 3:
        a = (g**k3) % P
        b = ((Y**k3)*M_i[i]) % P
        result_text.append(a)
        result_text.append(b)

for i in result_text:
    print(i, "", end="")

print()

ab: List[int] = result_text

pairs: List[List[int]] = [ab[i:i + 2] for i in range(0, len(ab), 2)]

result: List[str] = []
for pair in pairs:
    result.append(alphabet[eq(pair[0]**x, pair[1], P) - 1])

print (''.join(result))

