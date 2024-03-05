shared_n = int(input("Enter shared n:"))
shared_a = int(input("Enter shared a:"))

secret_1 = int(input("Enter secret_1:"))
secret_2 = int(input("Enter secret_2:"))

print("Publicly Shared Variables:")
print("  Publicly shared n: ", shared_n)
print("  Publicly shared a: ", shared_a)

Y_a = (shared_a ** secret_1) % shared_n
print("\n  Ya sended Over Public Chanel: ", Y_a)

Y_b = (shared_a ** secret_2) % shared_n
print("  Yb sended Over Public Chanel: ", Y_b)

print(" \n Privately Calculated Shared Secret:")

print("  Ka: ", (Y_b ** secret_1) % shared_n)

print("  Kb: ", (Y_a**secret_2) % shared_n)