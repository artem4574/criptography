from math import gcd
def EulerFunc(num):
    amount = 0
    for k in range(1, num + 1):
        if gcd(num, k) == 1:
            amount += 1
    return amount

def classic_Euclid(num_1, num_2):
    while num_1 != 0 and num_2 != 0:
        if num_1 >= num_2:
            num_1 %= num_2
        else:
            num_2 %= num_1
    return num_1 or num_2
