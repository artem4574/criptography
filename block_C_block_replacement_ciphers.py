def generate_table(keyword):
    start_alphabet = "АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЭЮЯ"
    keyword, count = "".join(keyword.split()).upper(), 0
    from collections import OrderedDict
    string_table = "".join(OrderedDict.fromkeys(keyword + start_alphabet))
    table = [[0]*6 for i in range(5)]
    for i in range (5):
        for j in range(6):
            table[i][j] = string_table[count]
            count+=1
            '''print(table[i][j], end='')
        print()'''
    return table


def find_index(array, element):
    flat_array = [item for sublist in array for item in sublist]
    try:
        index = flat_array.index(element)
        i = index // len(array[0])
        j = index % len(array[0])
        return (i, j)
    except ValueError:
        return None


text: str = str(input('Enter text: '))
key: str = str(input('Enter keyword(must not contain duplicate letters): '))
print(""" Select an action: 
            1. Encryption 
            2. Decryption""")
operation: int = int(input())
result_text, text, k = "", text.replace(' ', '').replace('й', 'и').replace('ь', 'ъ').replace('ё', 'е'), 0
table = generate_table(key)
if operation == 1:                               #encryption
    if len(text) % 2 != 0: text += "ф"                                    #избыточность для нечетной длины послеедовательности
    for i in range(0, len(text)-1, 2):
        f_let = text[i].upper()
        s_let = text[i+1].upper()
        if f_let == s_let:  text = text[:i+1] + "ф" + text[i+1:]         #избыточность для повторяющихся букв
        f_let_i, f_let_j = find_index(table, f_let)[0], find_index(table, f_let)[1]
        s_let_i, s_let_j = find_index(table, s_let)[0], find_index(table, s_let)[1]
        if f_let_i == s_let_i:                                           #если в таблице в одной строке
            result_text += table[f_let_i][(f_let_j + 1) % 6]
            result_text += table[s_let_i][(s_let_j + 1) % 6]
        if f_let_j == s_let_j:                                           #если в таблице в одном столбце
            result_text += table[(f_let_i + 1) % 5][f_let_j]
            result_text += table[(s_let_i + 1) % 5][s_let_j]
        else:
            result_text += table[f_let_i][s_let_j]
            result_text += table[s_let_i][f_let_j]
    print("Encrypted text: ", end=' ')
    for i in result_text:
        print(i, end='')
        k += 1
        if k % 5 == 0: print(" ", end='')
    print()
    print(text)
    exit()

if operation == 2:                     #decryption
    for i in range(0, len(text)-1, 2):
        f_let = text[i].upper()
        s_let = text[i+1].upper()
        f_let_i, f_let_j = find_index(table, f_let)[0], find_index(table, f_let)[1]
        s_let_i, s_let_j = find_index(table, s_let)[0], find_index(table, s_let)[1]
        if f_let_i == s_let_i:                                                   #если в таблице в одной строке
            result_text += table[f_let_i][(f_let_j - 1) % 6]
            result_text += table[s_let_i][(s_let_j - 1) % 6]
        if f_let_j == s_let_j:                                                   #если в таблице в одном столбце
            result_text += table[(f_let_i - 1) % 5][f_let_j]
            result_text += table[(s_let_i - 1) % 5][s_let_j]
        else:
            result_text += table[f_let_i][s_let_j]
            result_text += table[s_let_i][f_let_j]

    print("Decrypted text: ", end='')
    for i in result_text: print(i, end='')
    print()
    exit()
else:
     print("Error in select!")
     exit()

# РВ ЕБ КЖ ПЖ ВУ РМ ИШ МЗ ФУ ЯС ЗР ПС ПЖ ТЕ ГМ ФЩ ЛР ПЗ ФШ ЧТ ВН ЕИ ЕД ШН ФЩ МА МУ МЯ ЫХ ХИ ИШ ЗЩ ЩФ ФД