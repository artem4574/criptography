import copy
import sys
from itertools import zip_longest


list_alph = ["а", "б", "в", "г", "д", "е", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф",
             "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]


register_x = []
register_y = []
register_z = []


def digitization(open_text):
    dig_text = ""
    for i in range(len(open_text)):
        cipher = (list_alph.index(open_text[i]))
        cipher = int(cipher) + 1
        dig_text += (format(cipher, '06b'))
    return dig_text


def grouper(n, iterable, fill_value=None):
    args = [iter(iterable)] * n
    return zip_longest(fillvalue=fill_value, *args)


def undigitization(d_text):
    d_text = ' '.join(''.join(g) for g in grouper(6, d_text, ''))
    d_array = d_text.split()
    open_text = ""

    for i in d_array: open_text += (list_alph[int(str(int(i)), 2) - 1])

    return open_text


def loading_registers(key):

    reg_x_length = 19
    reg_y_length = 22
    reg_z_length = 23

    for i in range(reg_x_length):
        register_x.append(int(key[i]))

    p = reg_x_length

    for _ in range(reg_y_length):
        register_y.append(int(key[p]))
        p += 1

    k = reg_y_length + reg_x_length

    for _ in range(reg_z_length):
        register_z.append(int(key[k]))
        k += 1


def generate_key_stream(length):

    x_temp = copy.deepcopy(register_x)
    y_temp = copy.deepcopy(register_y)
    z_temp = copy.deepcopy(register_z)

    key_stream = []

    for _ in range(length):

        majority = (x_temp[8] + y_temp[10] + z_temp[10]) > 1

        if x_temp[8] == majority:
            new_bit = x_temp[13] ^ x_temp[16] ^ x_temp[17] ^ x_temp[18]
            x_temp = [new_bit] + x_temp[:-1]

        if y_temp[10] == majority:
            new_bit = y_temp[20] ^ y_temp[21]
            y_temp = [new_bit] + y_temp[:-1]

        if z_temp[10] == majority:
            new_bit = z_temp[7] ^ z_temp[20] ^ z_temp[21] ^ z_temp[22]
            z_temp = [new_bit] + z_temp[:-1]

        key_stream.append(x_temp[18] ^ y_temp[21] ^ z_temp[22])

    return key_stream


def decryption_format(dec_text):
    dec_text = dec_text.replace('тчк', '.').replace('зпт', ',').replace('прб', ' ')
    result = dec_text[0].upper() + dec_text[1:]
    result_list = list(result)
    for i in range(len(result_list) - 3):
        if result_list[i] == ".":
            result_list[i + 2] = result_list[i + 2].upper()

    result = ""
    for char in result_list: result += char

    return result


def A5_1(operation, text):

    key = str(input('Enter a 64-bit key: '))
    if len(key) != 64:
        print("Wrong key")
        exit()

    loading_registers(key)

    if operation == 1:

        ciphertext = ""

        binary = list(digitization(text))

        keystream = generate_key_stream(len(binary))

        for i in range(len(binary)): ciphertext += str(int(binary[i]) ^ keystream[i])

        print("Encrypted text: ", ' '.join(ciphertext[i: i + 5] for i in range(0, len(ciphertext), 5)))
        print()

    if operation == 2:

        dec_text = ""
        binary_xor = []
        keystream = generate_key_stream(len(text))

        for i in range(len(text)):
            binary_xor.insert(i, int(text[i]))
            dec_text += str(binary_xor[i] ^ keystream[i])

        analog = undigitization(dec_text)

        answer = decryption_format(analog)

        print("Decrypted text: ", end=' ')
        for i in answer: print(i, end='')
        print()


while True:

    print("""Select a cipher: 
             1.  A5/1
             2.  Exit
         """)
    select: int = int(input())
    if select == 2:
        sys.exit()

    if select not in [1, 2]:
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
        A5_1(operation, text.lower())
        print()

# 64-bit key: 0101001000011010110001110001100100101001000000110111111010110111
