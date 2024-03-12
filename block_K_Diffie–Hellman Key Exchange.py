import random

shared_n = int(input("Enter shared n (prime): "))
shared_a = int(input("Enter shared a: "))
if shared_a > shared_n:
    print("A > n")
    exit()
if shared_a <= 1 or shared_n <= 1:
    print("N and A should be > 1!")

secret_1: int = random.randint(2, shared_n - 1)
secret_2: int = random.randint(2, shared_n - 1)

print("Publicly Shared Variables:")
print("\n  Publicly shared n: ", shared_n)
print("  Publicly shared a: ", shared_a)

Y_a = (shared_a ** secret_1) % shared_n
Y_b = (shared_a ** secret_2) % shared_n

print("\n  Ya sended Over Public Chanel: ", Y_a)
print("  Yb sended Over Public Chanel: ", Y_b)

if Y_a == 1 or Y_b == 1:
    print("Open key = 1!")
    exit()

k_a = (Y_b ** secret_1) % shared_n
k_b = (Y_a**secret_2) % shared_n
print(" \nPrivately Calculated Shared Secret:")
print("  Ka: ", k_a)
print("  Kb: ", k_b)
