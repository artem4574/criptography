import sys


pi = [[12, 4, 6, 2, 10, 5, 11, 9, 14, 8, 13, 7, 0, 3, 15, 1],
      [6, 8, 2, 3, 9, 10, 5, 12, 1, 14, 4, 7, 11, 13, 0, 15],
      [11, 3, 5, 8, 2, 15, 10, 13, 14, 1, 7, 4, 12, 9, 6, 0],
      [12, 8, 2, 1, 13, 4, 15, 6, 7, 0, 10, 5, 3, 14, 9, 11],
      [7, 15, 5, 10, 8, 1, 6, 13, 0, 9, 3, 14, 11, 4, 2, 12],
      [5, 13, 15, 6, 9, 2, 12, 10, 11, 7, 8, 1, 4, 3, 14, 0],
      [8, 14, 2, 5, 6, 9, 1, 12, 15, 4, 11, 0, 13, 10, 3, 7],
      [1, 7, 14, 13, 0, 5, 8, 3, 4, 15, 10, 6, 9, 12, 11, 2]]


def t(x):
    y = 0
    for i in reversed(range(8)):
        j = (x >> 4 * i) & 0xf
        y <<= 4
        y ^= pi[i][j]
    return y


def g(x, k):
    def rot11(x):
        return ((x << 11) ^ (x >> (32 - 11))) & 2 ** 32 - 1

    return rot11(t((x + k) % 2 ** 32))


# k is 256-bits.
# The return value is a list of 32 keys of 32-bits each.
# The first 8 keys just come from the key k
# by partitioning k into eight 32-bit segments.
# The remaining keys are just repeats of these first 8 keys.
def magma_key_schedule(k):
    keys = []
    for i in reversed(range(8)):
        keys.append((k >> (32 * i)) & 2 ** 32 - 1)
    for i in range(8):
        keys.append(keys[i])
    for i in range(8):
        keys.append(keys[i])
    for i in reversed(range(8)):
        keys.append(keys[i])
    return keys


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


def magma(operation, text):

    key = int(input('Enter a 256-bit key: '), 16)
    if len(str(key)) != 64:
        print("Wrong key")
        exit()

    keys = magma_key_schedule(key)
    left_part, right_part = text >> 32, text & 2 ** 32 - 1
    if operation == 1:
        for i in range(31):
            (left_part, right_part) = (right_part, left_part ^ g(right_part, keys[i]))
        ciphertext = (left_part ^ g(right_part, keys[-1])) << 32 ^ right_part

        print("Encrypted text: ", ' '.join(ciphertext[i: i + 5] for i in range(0, len(ciphertext), 5)))
        print()

    if operation == 2:
        keys.reverse()

        for i in range(31):
            (left_part, right_part) = (right_part, left_part ^ g(right_part, keys[i]))
        result = (left_part ^ g(right_part, keys[-1])) << 32 ^ right_part

        answer = decryption_format(result)

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
        magma(operation, int(text, 16))
        print()

# key: ffeeddccbbaa99887766554433221100f0f1f2f3f4f5f6f7f8f9fafbfcfdfeff