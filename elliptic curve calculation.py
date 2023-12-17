from math import gcd
from pandas import *


# Сброс ограничений на количество выводимых рядов
pandas.set_option('display.max_rows', None)

# Сброс ограничений на число столбцов
pandas.set_option('display.max_columns', None)

# Сброс ограничений на количество символов в записи
pandas.set_option('display.max_colwidth', None)

def euler_func(num):
    amount = 0
    for k in range(1, num + 1):
        if gcd(num, k) == 1:
            amount += 1
    return amount


'''a = 1
b = 3
p = 41

print("D =", (-16 * (4 * a**3 + 27 * b**2)) % p)
print("J(E) =", int((1728 * (4 * a**3)) % p / ((4 * a**3 + 27 * b**2) % p)))

y2_mod_p = [0]*p
for i in range(p):
    y2_mod_p[i] = (i**2) % p
x_y_pair = []
array_of_points = []
for i in range(p):
    x = i
    y = (x**3+a*x+b) % p
    x_y_pair.append((x, y))
    if y in y2_mod_p:
        pair_1 = (x, (y2_mod_p.index(y) % p))
        pair_2 = (x, (-y2_mod_p.index(y) + p) % p)
        array_of_points.append(pair_1)
        if pair_1 != pair_2:
            array_of_points.append(pair_2)
for i in array_of_points: print(i)

points_map = (["0"]*(len(array_of_points)+1)  for i in range(p))
points_map = list(points_map)

for i in range(len(array_of_points)):
    points_map[0][i] = array_of_points[i]
    points_map[1][i] = array_of_points[i]

for j in range(len(array_of_points)):
    for k in range(2, p):
        if points_map[k - 1][j] == "O":
            points_map[k][j] = points_map[0][j]
            continue
        x_p = int(points_map[k-1][j][0])
        y_p = int(points_map[k-1][j][-1])
        x_q = int(points_map[0][j][0])
        y_q = int(points_map[0][j][-1])
        if points_map[k-1][j] == points_map[0][j]:
           try:
                delta = (3 * (x_p**2) + a) % p / (2 * y_p) % p
                if delta % 1 != 0: delta = ((3 * (x_p**2) + a) % p) * ((((2 * y_p) % p) ** (euler_func(p)-1)) % p) % p
           except ZeroDivisionError:
               points_map[k][j] = "O"
               continue
        else:
            if y_p == -y_q or -y_p == y_q:
                points_map[k][j] = "O"
                continue
            else:
                try:
                    delta = (((y_q - y_p) % p)/((x_q - x_p) % p)) % p
                    if delta % 1 != 0: delta = (((y_q - y_p) % p) * (((x_q - x_p) % p) ** (euler_func(p) - 1)) % p)
                except ZeroDivisionError:
                    points_map[k][j] = "O"
                    continue
        x_r = (delta ** 2 - x_p - x_q) % p
        y_r = (((delta * (x_p - x_r)) % p) - y_p) % p
        points_map[k][j] = (int(x_r), int(y_r))
        #print(x_p, y_p, x_q, y_q, x_r, y_r, delta)

for i in range(p-1):
    print(i+1, "  ",end='')
    for j in range(len(array_of_points)):
        print(points_map[i][j], " ", end='')
    print()
print(DataFrame(points_map))'''

def composition(point, k, a, p):
    ans_point = point
    delta = (((3 * point[0] ** 2 + a) % p) / ((2 * point[1]) % p)) % p
    if delta % 1 != 0: delta = ((3 * (ans_point[0]**2) + a) % p) * ((((2 * ans_point[1]) % p) ** (euler_func(p)-1)) % p) % p
    x = (delta ** 2 - 2 * ans_point[0]) % p
    y = (delta * (ans_point[0] - x) - ans_point[1]) % p
    ans_point = [int(x), int(y)]
    if k > 2: 
        x_q = int(point[0])
        y_q = int(point[1])
        for i in range(k-2):
            if ans_point == "O":
                ans_point = point
                continue
            x_p = int(ans_point[0])
            y_p = int(ans_point[1])
            if point == ans_point:
                try:
                    delta = (3 * (x_p**2) + a) % p / (2 * y_p) % p
                    if delta % 1 != 0: delta = ((3 * (x_p**2) + a) % p) * ((((2 * y_p) % p) ** (euler_func(p)-1)) % p) % p
                except ZeroDivisionError:
                    ans_point = "O"
                    continue
            else:
                if y_p == -y_q or -y_p == y_q:
                    ans_point = "O"
                    continue
                else:
                    try:
                        delta = (((y_q - y_p)%p)/((x_q - x_p)%p)) % p
                        if delta % 1 != 0: delta = (((y_q - y_p) % p) * (((x_q - x_p) % p) ** (euler_func(p) - 1)) % p)
                    except ZeroDivisionError:
                        ans_point = "O"
                        continue
            x_r = (delta ** 2 - x_p - x_q) % p
            y_r = (((delta * (x_p - x_r)) % p) - y_p) % p
            ans_point = (int(x_r), int(y_r))

    if type(ans_point) is list:
        print("Composition: [", k, "]", "(", point[0], ",", point[1], ")", " = (", ans_point[0], ",", ans_point[1], ")", sep = '' )
    else: 
        print("Composition: [", k, "]", "(", point[0], ",", point[1], ")", " = ", ans_point, sep = '' )
for i in range(2, 13):
    composition([0,1], i, 1, 11)


