from collections import OrderedDict
import numpy as np
from block_A_simple_replacement_ciphers import decryption_format


def generate_table(keyword):

    start_alphabet = "абвгдежзиклмнопрстуфхцчшщъыэюя"
    keyword, count = "".join(keyword.split()), 0
    string_table = "".join(OrderedDict.fromkeys(keyword + start_alphabet))
    table = [[0] * 6 for _ in range(5)]

    for i in range(5):
        for j in range(6):
            table[i][j] = string_table[count]
            count += 1

    return table


def find_index(array, element):
    flat_array = [item for sublist in array for item in sublist]
    try:
        return flat_array.index(element) // len(array[0]), flat_array.index(element) % len(array[0])
    except ValueError:
        return None


def Playfair_cipher(operation, text):

    key: str = str(input('Enter keyword(must not contain duplicate letters): '))
    if len(key) != len(set(key)):
        print("Wrong key!")
        exit()
    text = text.replace('й', 'и').replace('ь', 'ъ').replace('ё', 'е').replace(' ', '')
    table = generate_table(key)
    answer = ''

    if operation == 1:

        for i in range(len(text) - 1):
            if text[i] == text[i + 1]:
                text = text[:i + 1] + "ф" + text[i + 1:]

        if len(text) % 2 != 0:
            text += "ф"

        i = 0

        while i < len(text):

            f_let = text[i]
            s_let = text[i + 1]

            i += 2

            f_let_i, f_let_j = find_index(table, f_let)[0], find_index(table, f_let)[1]
            s_let_i, s_let_j = find_index(table, s_let)[0], find_index(table, s_let)[1]

            if f_let_i == s_let_i:                              # если в таблице в одной строке
                answer += table[f_let_i][(f_let_j + 1) % 6]
                answer += table[s_let_i][(s_let_j + 1) % 6]
                continue

            if f_let_j == s_let_j:                               # если в таблице в одном столбце
                answer += table[(f_let_i + 1) % 5][f_let_j]
                answer += table[(s_let_i + 1) % 5][s_let_j]
                continue

            if f_let_i != s_let_i and f_let_j != s_let_j:
                answer += table[f_let_i][s_let_j]
                answer += table[s_let_i][f_let_j]
                continue

        print("Encrypted text: ", ' '.join(answer[i: i + 5] for i in range(0, len(answer) - 1 if len(text) % 2 == 1 else len(answer), 5)))
        print()

    if operation == 2:

        for i in range(0, len(text) - 1, 2):

            f_let = text[i]
            s_let = text[i + 1]

            f_let_i, f_let_j = find_index(table, f_let)[0], find_index(table, f_let)[1]
            s_let_i, s_let_j = find_index(table, s_let)[0], find_index(table, s_let)[1]

            if f_let_i == s_let_i:                            # если в таблице в одной строке
                answer += table[f_let_i][(f_let_j - 1) % 6]
                answer += table[s_let_i][(s_let_j - 1) % 6]
                continue

            if f_let_j == s_let_j:                            # если в таблице в одном столбце
                answer += table[(f_let_i - 1) % 5][f_let_j]
                answer += table[(s_let_i - 1) % 5][s_let_j]
                continue

            if f_let_i != s_let_i and f_let_j != s_let_j:
                answer += table[f_let_i][s_let_j]
                answer += table[s_let_i][f_let_j]
                continue

        result = decryption_format(answer)

        print("Decrypted text: ", result[:-1] if result[-1] == 'ф' else result, end='')
        print()


def matrix_cipher(operation, text):

    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    key_matrix = np.zeros((3, 3))

    print("Enter 3x3 matrix via enter:")
    for rows in range(3):
        row = input().split()
        for cols in range(3): key_matrix[rows, cols] = int(row[cols])

    answer = ""

    if np.linalg.det(key_matrix) not in [0, 6.66133814775094e-16]:

        if operation == 1:

            text += "ф" * ((3 - len(text) % 3) % 3)

            for i in range(0, len(text), 3):

                cur_matrix = np.zeros((3, 1))

                for j in range(3): cur_matrix[j, 0] = alphabet.index(text[j + i]) + 1

                l_matrix = np.matmul(key_matrix, cur_matrix)

                for k in range(3): answer += str(int(l_matrix[k, 0])) + " "

            print("Encrypted text: ", answer)
            print()

        else:                                                              

            ciphertext, enc_text = text.split(" "), []
            key_matrix = np.linalg.inv(key_matrix)

            for i in range(0, len(ciphertext), 3):

                cur_matrix = np.zeros((3, 1))

                for j in range(3):
                    cur_matrix[j, 0] = int(ciphertext[j + i])

                l_matrix = np.matmul(key_matrix, cur_matrix)

                for pos in range(3):
                    enc_text.append(round(l_matrix[pos, 0]) - 1)

            for i in range(len(enc_text)):
                answer += alphabet[int(enc_text[i])]

            answer = decryption_format(answer)
            while answer[-1] == "ф": answer = answer[:-1]

            print("Decrypted text: ", answer, end='')
            print()

    else:
        print("Error! Determinant = 0")
        exit()


'''
import sys
while True:

    print("""Select a cipher: 
             1.  Playfair cipher
             2.  Matrix cipher
             3.  Exit
         """)
    select: int = int(input())
    if select == 3:
        sys.exit()

    if select not in [1, 2, 3]:
        print("Wrong select!")
        continue

    print(""" Select an action: 
                1. Encryption 
                2. Decryption""")
    operation: int = int(input())
    if operation not in [1, 2]:
        print("Wrong select!")
        continue

    text: str = str(input('Enter text: '))
    print()

    if operation == 1:
        for i in range(len(text)):

            if text.find('.') != -1:
                index = text.find('.')
                str1_split1 = text[:index]
                str1_split2 = text[index + 1:]
                text = str1_split1 + 'тчк' + str1_split2

            if text.find(',') != -1:
                index = text.find(',')
                str1_split1 = text[:index]
                str1_split2 = text[index + 1:]
                text = str1_split1 + 'зпт' + str1_split2

            if text.find(' ') != -1:
                index = text.find(' ')
                str1_split1 = text[:index]
                str1_split2 = text[index + 1:]
                text = str1_split1 + 'прб' + str1_split2

    elif select == 1:
        text = text.replace(' ', '')

    if select == 1:
        Playfair_cipher(operation, text.lower())
        print()

    if select == 2:
        matrix_cipher(operation, text.lower())
        print()
'''