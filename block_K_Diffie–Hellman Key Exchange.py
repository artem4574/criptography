
shared_n = 62
shared_a = 14

secret_1 = 5
secret_2 = 15

print("Publicly Shared Variables:")
print("  Publicly Shared n: ", shared_n)
print("  Publicly Shared a: ", shared_a)

Y_a = (shared_a ** secret_1) % shared_n
print("\n  Ya Sended Over Public Chanel: ", Y_a)

Y_b = (shared_a ** secret_2) % shared_n
print("  Yb Sended Over Public Chanel: ", Y_b)

print(" \n Privately Calculated Shared Secret:")

shared_secret_1 = (Y_b ** secret_1) % shared_n
print("  Ka: ", shared_secret_1)

shared_secret_2 = (Y_a**secret_2) % shared_n
print("  Kb: ", shared_secret_2)