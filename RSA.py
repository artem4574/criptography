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

print(3**59 % 60)
print(22**27 % 77)
def eq(a: int, b: int, m: int) -> int:
    q: List[int] = euclid(a, m)
    if (m < a): q.insert(0, 0)
    P: List = [1, q[0]]
    for i in range(1, len(q)): P.append(P[i]*q[i]+P[i-1])
    return ((-1)**(len(q) - 1) * P[-2] * b) % m

def digitization(open_text, result = []):
    for i in range(len(open_text)): result.append(alphabet.index(open_text[i])+1)
    return result

p = int(input(" - Enter P(prime): "))
q = int(input(" - Enter Q(another prime): "))
n = p * q
phi = (p-1) * (q-1)
E = int(input(" - Enter E: "))
D = eq(E, 1, phi)
print(D)
text = input(" - Enter a text: ")

print(""" Select an action: 
    1. Encryption 
    2. Decryption""")
choose: int = int(input())
if choose == 1:

    digit_text = digitization(text.replace(' ', ''))
    ciphertext = []

    for i in range(len(digit_text)): ciphertext.append((digit_text[i] ** E) % n)
    for i in ciphertext:
        print(i, "", end="")
    print()
if choose == 2:
    text: List[int] = text.split()
    result_text = ""
    for i in text: result_text += alphabet[((int(i) ** D) % n) - 1]
    print(result_text)
    print()
else:
     print("Error in select!")
     exit()
