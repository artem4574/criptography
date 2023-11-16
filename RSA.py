import random


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def mod_inverse(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True


def generate_key_pair(p, q):
    if not (is_prime(p) and is_prime(q)): raise ValueError('Both numbers must be prime.')
    elif p == q: raise ValueError('p and q cannot be equal')
    n = p * q
    phi = (p-1) * (q-1)
    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    d = mod_inverse(e, phi)
    return ((e, n), (d, n))


def encrypt(pk, plaintext):
    key, n = pk
    cipher = [pow(ord(char), key, n) for char in plaintext]
    return cipher


def decrypt(pk, ciphertext):
    key, n = pk
    aux = [str(pow(char, key, n)) for char in ciphertext]
    plain = [chr(int(char2)) for char2 in aux]
    return ''.join(plain)


p = int(input(" - Enter a prime number: "))
q = int(input(" - Enter another prime number (not one you entered above): "))

public, private = generate_key_pair(p, q)

print(" - Your public key is ", public, " and your private key is ", private)

message = input(" - Enter a message to encrypt with your public key: ")
encrypted_msg = encrypt(public, message.replace(' ', ''))

print(" - Your encrypted message is: ", ''.join(map(lambda x: str(x), encrypted_msg)))
print(" - Decrypting message with private key ", private, " . . .")
print(" - Your message is: ", decrypt(private, encrypted_msg))
