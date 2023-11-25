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


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def comparisons (a, b, m):
    print("Comparison: ", a, "X", " ≡ ", b, " (mod", m,")", sep='')
    print("M % A = ")
    divider,divisible = m, a
    rem = divider % divisible
    n, arr_q = 0,[]
    while rem !=0:
        integer = divider // divisible
        rem = divider % divisible
        arr_q.append(integer)
        print(divider, "/", divisible, " = ", integer, "(", rem, ")", sep='')
        divider, divisible = divisible, rem
        n+=1
    print("n     ", end='')
    for i in range(n): print(i, "  ", end='')
    print("\nq     ", end='')
    for i in arr_q: print(i, "  ", end='')
    print("\nP  1 ", arr_q[0],"  ", end='')
    p = [1, arr_q[0]]
    for i in range(2,n+1):
        p.append(arr_q[i-1]*p[i-1]+p[i-2])
        print(p[i], " ", end='')
comparisons(54,27,579)
