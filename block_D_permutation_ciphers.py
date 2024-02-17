import sys


def decryption_format(dec_text):
    dec_text = dec_text.replace('тчк', '.').replace('зпт', ',').replace('прб', ' ')
    result = dec_text[0].upper() + dec_text[1:]
    result_list = list(result)
    for i in range(len(result_list) - 3):
        if result_list[i] == ".":
            result_list[i + 2] = result_list[i + 2].upper()
    result = ""
    for char in result_list:
        result += char
    return result


def mirror_matrix_1(matrix):
    def reverse(row):
        return row[::-1]

    mirrored_matrix = [reverse(row) for row in matrix]
    return mirrored_matrix


def mirror_matrix_2(matrix):
    str_0, str_1, str_2 = matrix[0], matrix[1], matrix[2]
    matrix[0], matrix[1], matrix[2] = matrix[5], matrix[4], matrix[3]
    matrix[3], matrix[4], matrix[5] = str_2, str_1, str_0
    return matrix


def Cardano_grid(operation, text, k=0):
    result_text = ""
    if len(text) > 60:
        grid_10 = [
            [0, 1, 0, 0, 0, 0, 1, 0, 0, 1],
            [1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 1, 0, 0, 1, 0],
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
            [1, 0, 0, 1, 0, 1, 1, 0, 0, 1],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 1, 0, 1, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0]]

        if operation == 1:                                                # encryption >= 60

            while len(text) != 0:

                table_arr = [[0] * 10 for _ in range(10)]

                for i in range(10):
                    for j in range(10):
                        if len(text) != 0:
                            table_arr[i][j] = text[0]
                            text = text[1:]
                        else:
                            table_arr[i][j] = "я"

                for i in range(10):
                    for j in range(10):
                        if grid_10[i][j] == 1:
                            result_text += str(table_arr[i][j])

                for i in range(10):
                    for j in range(10):
                        if grid_10[10 - j - 1][i] == 1:
                            result_text += str(table_arr[i][j])

                for i in range(10):
                    for j in range(10):
                        if grid_10[10 - i - 1][10 - j - 1] == 1:
                            result_text += str(table_arr[i][j])

                for i in range(10):
                    for j in range(10):
                        if grid_10[j][10 - i - 1] == 1:
                            result_text += str(table_arr[i][j])

            print("Encrypted text: ", end=' ')
            for i in result_text:
                print(i, end='')
                k += 1
                if k % 5 == 0: print(" ", end='')
            print()

        if operation == 2:                                             # decryption >= 60

            while len(text) != 0:

                table_arr = [[0] * 10 for _ in range(10)]

                for i in range(10):
                    for j in range(10):
                        if grid_10[i][j] == 1:
                            if len(text) != 0:
                                table_arr[i][j] = text[0]
                                text = text[1:]
                            else:
                                table_arr[i][j] = "я"

                for i in range(10):
                    for j in range(10):
                        if grid_10[10 - j - 1][i] == 1:
                            if len(text) != 0:
                                table_arr[i][j] = text[0]
                                text = text[1:]
                            else:
                                table_arr[i][j] = "я"

                for i in range(10):
                    for j in range(10):
                        if grid_10[10 - i - 1][10 - j - 1] == 1:
                            if len(text) != 0:
                                table_arr[i][j] = text[0]
                                text = text[1:]
                            else:
                                table_arr[i][j] = "я"

                for i in range(10):
                    for j in range(10):
                        if grid_10[j][10 - i - 1] == 1:
                            if len(text) != 0:
                                table_arr[i][j] = text[0]
                                text = text[1:]
                            else:
                                table_arr[i][j] = "я"

                for i in range(10):
                    for j in range(10):
                        result_text += str(table_arr[i][j])

            answer = decryption_format(result_text)
            while answer[-1] in ["я", "Я"]: answer = answer[:-1]

            print("Decrypted text: ", end=' ')
            for i in answer: print(i, end='')
            print()

    else:
        grid_6 = [
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 1, 0, 1, 1, 0, 0],
            [0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
            [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 1, 1, 0, 0, 1]]

        table_arr = [[0] * 10 for _ in range(6)]

        if operation == 1:                                         # encryption <= 60

            for i in range(6):
                for j in range(10):
                    if grid_6[i][j] == 1:
                        if len(text) != 0:
                            table_arr[i][j] = text[0]
                            text = text[1:]
                        else:
                            table_arr[i][j] = "я"

            grid_st_2 = mirror_matrix_1(grid_6)

            for i in range(6):
                for j in range(10):
                    if grid_st_2[i][j] == 1:
                        if len(text) != 0:
                            table_arr[i][j] = text[0]
                            text = text[1:]
                        else:
                            table_arr[i][j] = "я"

            grid_st_3 = mirror_matrix_2(grid_st_2)

            for i in range(6):
                for j in range(10):
                    if grid_st_3[i][j] == 1:
                        if len(text) != 0:
                            table_arr[i][j] = text[0]
                            text = text[1:]
                        else:
                            table_arr[i][j] = "я"

            grid_st_4 = mirror_matrix_2(grid_6)

            for i in range(6):
                for j in range(10):
                    if grid_st_4[i][j] == 1:
                        if len(text) != 0:
                            table_arr[i][j] = text[0]
                            text = text[1:]
                        else:
                            table_arr[i][j] = "я"

            for i in range(6):
                for j in range(10):
                    result_text += str(table_arr[i][j])

            print("Encrypted text: ", end=' ')

            for i in result_text:
                print(i, end='')
                k += 1
                if k % 5 == 0: print(" ", end='')
            print()

        if operation == 2:                                            # decryption <= 60

            for i in range(6):
                for j in range(10):
                    if len(text) != 0:
                        table_arr[i][j] = text[0]
                        text = text[1:]
                    else:
                        table_arr[i][j] = "я"

            for i in range(6):
                for j in range(10):
                    if grid_6[i][j] == 1:
                        result_text += table_arr[i][j]

            grid_st_2 = mirror_matrix_1(grid_6)

            for i in range(6):
                for j in range(10):
                    if grid_st_2[i][j] == 1:
                        result_text += table_arr[i][j]

            grid_st_3 = mirror_matrix_2(grid_st_2)

            for i in range(6):
                for j in range(10):
                    if grid_st_3[i][j] == 1:
                        result_text += table_arr[i][j]

            grid_st_4 = mirror_matrix_2(grid_6)

            for i in range(6):
                for j in range(10):
                    if grid_st_4[i][j] == 1:
                        result_text += table_arr[i][j]

            answer = decryption_format(result_text)
            while answer[-1] in ["я", "Я"]: answer = answer[:-1]

            print("Decrypted text: ", end=' ')
            for i in answer: print(i, end='')
            print()


def vertical_permutation(operation, text, k=0):
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    key = input("Enter key: ")
    result_text = ""

    if len(set(key)) != len(key):
        print("Wrong key!")
        exit()

    cols = len(key)
    rows = int(len(text) / cols) + 1

    table = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if len(text) != 0:
                table[i][j] = text[0]
                text = text[1:]
            else:
                table[i][j] = "я"

    key_list = [0 for _ in range(len(key))]
    key_set = [char for char in key]
    counter = 0

    for i in alphabet:
        if i in key_set:
            key_list[key_set.index(i)] = counter
            counter += 1

    if operation == 1:
        for i in range(rows):
            for j in range(cols):
                result_text += table[i][key_list[j]]

        print("Encrypted text: ", end=' ')
        for i in result_text:
            print(i, end='')
            k += 1
            if k % 5 == 0: print(" ", end='')
        print()

    if operation == 2:

        for i in range(rows):
            for j in range(cols):
                result_text += table[i][key_list.index(j)]

        answer = decryption_format(result_text)
        while answer[-1] in ["я", "Я"]: answer = answer[:-1]

        print("Decrypted text: ", end=' ')
        for i in answer: print(i, end='')
        print()


while True:

    print("""Select a cipher: 
             1.  Cardano grid
             2.  Vertical permutation
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

    else:
        text = text.replace(' ', '')

    if select == 1:
        Cardano_grid(operation, text.lower())
        print()

    if select == 2:
        vertical_permutation(operation, text.lower())
        print()
