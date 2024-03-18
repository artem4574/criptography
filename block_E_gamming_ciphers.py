import math
from block_A_simple_replacement_ciphers import decryption_format
from block_A_simple_replacement_ciphers import listalf as list_alph


def digitization_for_Shannon(open_text):
    result = []
    for i in range(len(open_text)): result.append(list_alph.index(open_text[i]) + 1)
    return result


def undigitization_for_Shannon(ciphertext):
    result = ""
    for i in range(len(ciphertext)): result += (list_alph[ciphertext[i] - 1])
    return result


def generate_gamma_for_Shannon(a, c, t0, length):
    t, gamma = t0, []
    for i in range(length):
        gamma.append((a * t + c) % 32)
        t = (a * t + c) % 32
    return gamma


def Shannon_notebook(operation, text):

    a, c, t0 = int(input("Enter the value of a (a % 2 = 1): ")), int(
        input("Enter the value of c (coprime with 32): ")) % 32, int(input("Enter the value of T0: "))

    if a % 2 != 1 or math.gcd(c, 32) != 1 or a % 4 == 1:
        print("Wrong key!")
        exit()

    # a, c, t0 = 5, 9, 14

    digital_text = digitization_for_Shannon(text)

    gen_gamma = generate_gamma_for_Shannon(a, c, t0, len(digital_text))

    if operation == 1:

        encrypted_text = []

        for i in range(len(digital_text)): encrypted_text.append((digital_text[i] + gen_gamma[i]) % 32)

        ciphertext = undigitization_for_Shannon(encrypted_text)

        print("Encrypted text: ", ' '.join(ciphertext[i: i + 5] for i in range(0, len(ciphertext), 5)))
        print()

    if operation == 2:

        dec_text = [0] * len(digital_text)

        for i in range(len(digital_text)):

            if gen_gamma[i] < digital_text[i]: dec_text[i] = digital_text[i] - gen_gamma[i]

            else: dec_text[i] = digital_text[i] + 32 - gen_gamma[i]

        open_text = undigitization_for_Shannon(dec_text)

        answer = decryption_format(open_text)

        print("Decrypted text: ", answer)
        print()


'''
import sys
while True:

    print("""Select a cipher: 
             1.  Shannon's notebook
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
        Shannon_notebook(operation, text.lower())
        print()
'''