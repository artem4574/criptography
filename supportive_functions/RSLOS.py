from itertools import zip_longest
import numpy
import sys


list_alph = ["а", "б", "в", "г", "д", "е", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф",
             "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]


def xor(scr, register):
    for_xor_scr = []  # массив единиц scrambler
    for_xor_reg = []  # массив регистра
    buffer = []       # буфер битов для xor
    for i in range(len(scr)): for_xor_scr.append(int(scr[i]))
    for i in range(len(register)): for_xor_reg.append(int(register[i]))
    for i in range(len(scr)):
        if for_xor_scr[i] == 1: buffer.append(for_xor_reg[i])
    return str(numpy.bitwise_xor.reduce(buffer)) + register[:-1]


def grouper(n, iterable, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(fillvalue=fillvalue, *args)




def digitization_for_rslos(open_text):
    dig_text = ""
    for i in range(len(open_text)):
        cipher = (list_alph.index(open_text[i]))
        cipher = int(cipher) + 1
        dig_text += (format(cipher, '06b'))
    return dig_text


def undigitization_for_rslos(d_text):
    d_text = ' '.join(''.join(g) for g in grouper(6, d_text, ''))
    d_array = d_text.split()
    open_text = ""
    # for i in d_array: print(i, " ", end='')
    for i in d_array:
        open_text += (list_alph[int(str(int(i)), 2) - 1])
        # print(int(str(int(i)), 2), " ", end='')
    return open_text


def gamming(text, reg1, reg2, scrambler1, scrambler2):
    result_str = ""
    for i in range(len(text)):
        ex_bit1 = reg1[len(reg1) - 1]
        ex_bit2 = reg2[len(reg2) - 1]

        code_bit = int(ex_bit1) ^ int(ex_bit2)
        res_bit = int(text[i]) ^ code_bit

        result_str += str(res_bit)
        # print(reg1, " ", ex_bit1, " ", reg2, " ", ex_bit2, " ", code_bit, " ", text[i], " ", res_bit)

        reg1 = xor(scrambler1, reg1)
        reg2 = xor(scrambler2, reg2)

    return result_str



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


def RSLOS(operation, text):

    scrambler1: str = str(input('Enter scrambler_1: '))
    scrambler2: str = str(input('Enter scrambler_2: '))

    reg1: str = str(input('Enter key_1: '))
    reg2: str = str(input('Enter key_2: '))

    if operation == 1:

        d_text = digitization_for_rslos(text)
        result_str = gamming(d_text, reg1, reg2, scrambler1, scrambler2)

        print("Cipher text:")
        result_str = ' '.join(''.join(g) for g in grouper(5, result_str, ''))
        result_array = result_str.split()

        for i in range(len(result_array)):
            print(result_array[i], " ", end='')
            if i % 15 == 14: print()

    if operation == 2:

        dig_text = gamming((text.replace(' ', '')), reg1, reg2, scrambler1, scrambler2)

        print("Decrypted text: ", undigitization_for_rslos(dig_text))



while True:

    print("""Select a cipher:
             1.  Shannon's notebook
             2.  RSLOS
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
        RSLOS(operation, text.lower())
        print()

'''
scrambler1 = 10110
scrambler2 = 1001
key1 = 10110
key2 = 1001
open text = одиндуракможетбольшеспрашиватьзптчемдесятьумныхответитьтчк
dig_text = 001111000101001001001110000101010100010001000001001011001101001111000111000110010011000010001111001100011101011001000110010010010000010001000001011001001001000011000001010011011101001000010000010011011000000110001101000101000110010010100000010011011101010100001101001110011100010110001111010011000011000110010011001001010011011101010011011000001011
encrypted text = 11000  01000  01101  10011  10111  10111  11110  11100  10101  00100  00111  11011  00110  11001  11001 00010  01010  10110  01100  00011  01100  00011  00000  00011  00111  11000  01010  10100  01111  10100  11000  11010  10011  00110  00100  00100  10001  00101  01000  10111  00101  00101  10111  00101  10010  11111  01011  11110  11010  01001  01000  11000  11001  01110  01100  11110  11111  10010  00011  11100   01001  01101  00001  01001  10000  01101  10111  10110  10010  000
'''
