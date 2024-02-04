def mirror_matrix_1(matrix):
    def reverse(row):
        return row[::-1]
    mirrored_matrix = [reverse(row) for row in matrix]
    return mirrored_matrix


def mirror_matrix_2(matrix):
    str_0 = matrix[0]
    str_1 = matrix[1]
    str_2 = matrix[2]
    matrix[0] = matrix[5]
    matrix[1] = matrix[4]
    matrix[2] = matrix[3]
    matrix[3] = str_2
    matrix[4] = str_1
    matrix[5] = str_0
    return matrix


def Cardano_grid():
    text: str = str(input('Enter text: '))
    print(""" Select an action:
                        1. Encryption
                        2. Decryption""")
    operation: int = int(input())
    text, k = text.replace(' ', ''), 0

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
        size_i = 10
        size_j = 10
        result_text = ""
        table_arr = [[0] * 10 for i in range(10)]
        if operation == 1:                                      # encryption_10
                for i in range(size_i):
                    for j in range(size_j):
                        if len(text)!=0:
                            table_arr[i][j] = text[0]
                            text = text[1:]
                        else: table_arr[i][j] = "я"

                for i in range(size_i):
                    for j in range(size_j):
                        if grid_10[i][j] == 1:
                            result_text += table_arr[i][j]

                for i in range(size_i):
                    for j in range(size_j):
                        if grid_10[size_i - j - 1][i] == 1:
                            result_text += table_arr[i][j]

                for i in range(size_i):
                    for j in range(size_j):
                        if grid_10[size_i - i - 1][size_i - j - 1] == 1:
                            result_text += table_arr[i][j]

                for i in range(size_i):
                    for j in range(size_j):
                        if grid_10[j][size_i - i - 1] == 1:
                            result_text += table_arr[i][j]

                print("Encrypted text: ", end=' ')
                for i in result_text:
                    print(i, end='')
                    k += 1
                    if k % 5 == 0: print(" ", end='')
                print()
                exit()
        if operation == 2:                                     # decryption_10

            for i in range(size_i):
                for j in range(size_j):
                    if grid_10[i][j] == 1:
                        if len(text)!=0:
                            table_arr[i][j] = text[0]
                            text = text[1:]
                        else:
                            table_arr[i][j] = "я"

            for i in range(size_i):
                for j in range(size_j):
                    if grid_10[size_i - j - 1][i] == 1:
                        if len(text) != 0:
                            table_arr[i][j] = text[0]
                            text = text[1:]
                        else:
                            table_arr[i][j] = "я"

            for i in range(size_i):
                for j in range(size_j):
                    if grid_10[size_i - i - 1][size_i - j - 1] == 1:
                        if len(text) != 0:
                            table_arr[i][j] = text[0]
                            text = text[1:]
                        else:
                            table_arr[i][j] = "я"

            for i in range(size_i):
                for j in range(size_j):
                    if grid_10[j][size_i - i - 1] == 1:
                        if len(text) != 0:
                            table_arr[i][j] = text[0]
                            text = text[1:]
                        else:
                            table_arr[i][j] = "я"

            for i in range(size_i):
                for j in range(size_j):
                    result_text += str(table_arr[i][j])

            print("Decrypted text: ", end=' ')
            for i in result_text: print(i, end='')
            print()
            exit()
        else:
            print("Error in select!")
            exit()

    else:
        grid_6 = [
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 1, 0, 1, 1, 0, 0],
            [0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
            [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 1, 1, 0, 0, 1]]
        size_i = 6
        size_j = 10
        result_text = ""
        table_arr = [[0] * 10 for i in range(6)]

        if operation == 1:                                         # encryption_10

            for i in range(size_i):
                for j in range(size_j):
                    if grid_6[i][j] == 1:
                        if len(text) != 0:
                            table_arr[i][j] = text[0]
                            text = text[1:]
                        else:
                            table_arr[i][j] = "я"

            grid_st_2 = mirror_matrix_1(grid_6)

            for i in range(size_i):
                for j in range(size_j):
                    if grid_st_2[i][j] == 1:
                        if len(text) != 0:
                            table_arr[i][j] = text[0]
                            text = text[1:]
                        else:
                            table_arr[i][j] = "я"

            grid_st_3 = mirror_matrix_2(grid_st_2)

            for i in range(size_i):
                for j in range(size_j):
                    if grid_st_3[i][j] == 1:
                        if len(text) != 0:
                            table_arr[i][j] = text[0]
                            text = text[1:]
                        else:
                            table_arr[i][j] = "я"

            grid_st_4 = mirror_matrix_2(grid_6)

            for i in range(size_i):
                for j in range(size_j):
                    if grid_st_4[i][j] == 1:
                        if len(text) != 0:
                            table_arr[i][j] = text[0]
                            text = text[1:]
                        else:
                            table_arr[i][j] = "я"

            for i in range(size_i):
                for j in range(size_j):
                    result_text += str(table_arr[i][j])

            print("Encrypted text: ", end=' ')

            for i in result_text:
                print(i, end='')
                k += 1
                if k % 5 == 0: print(" ", end='')
            print()
            exit()

        if operation == 2:                                     # decryption_10

            for i in range(size_i):
                for j in range(size_j):
                    if len(text) != 0:
                        table_arr[i][j] = text[0]
                        text = text[1:]
                    else:
                        table_arr[i][j] = "я"

            for i in range(size_i):
                for j in range(size_j):
                    if grid_6[i][j] == 1:
                        result_text += table_arr[i][j]

            grid_st_2 = mirror_matrix_1(grid_6)

            for i in range(size_i):
                for j in range(size_j):
                    if grid_st_2[i][j] == 1:
                        result_text += table_arr[i][j]

            grid_st_3 = mirror_matrix_2(grid_st_2)

            for i in range(size_i):
                for j in range(size_j):
                    if grid_st_3[i][j] == 1:
                       result_text += table_arr[i][j]

            grid_st_4 = mirror_matrix_2(grid_6)

            for i in range(size_i):
                for j in range(size_j):
                    if grid_st_4[i][j] == 1:
                        result_text += table_arr[i][j]

            print("Decrypted text: ", end=' ')
            for i in result_text:
                print(i, end='')
            print()
            exit()
        else:
            print("Error in select!")
            exit()

Cardano_grid()
