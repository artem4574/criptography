import random
import binascii
import pickle
from os.path import dirname
from block_A_simple_replacement_ciphers import decryption_format
from block_A_simple_replacement_ciphers import listalf as list_alph


pi = [[12, 4, 6, 2, 10, 5, 11, 9, 14, 8, 13, 7, 0, 3, 15, 1],
      [6, 8, 2, 3, 9, 10, 5, 12, 1, 14, 4, 7, 11, 13, 0, 15],
      [11, 3, 5, 8, 2, 15, 10, 13, 14, 1, 7, 4, 12, 9, 6, 0],
      [12, 8, 2, 1, 13, 4, 15, 6, 7, 0, 10, 5, 3, 14, 9, 11],
      [7, 15, 5, 10, 8, 1, 6, 13, 0, 9, 3, 14, 11, 4, 2, 12],
      [5, 13, 15, 6, 9, 2, 12, 10, 11, 7, 8, 1, 4, 3, 14, 0],
      [8, 14, 2, 5, 6, 9, 1, 12, 15, 4, 11, 0, 13, 10, 3, 7],
      [1, 7, 14, 13, 0, 5, 8, 3, 4, 15, 10, 6, 9, 12, 11, 2]]


def g(x, k):

    def rot11(x):
        return ((x << 11) ^ (x >> (32 - 11))) & 2 ** 32 - 1

    def t(x):
        y = 0
        for i in reversed(range(8)):
            j = (x >> 4 * i) & 0xf
            y <<= 4
            y ^= pi[i][j]
        return y

    return rot11(t((x + k) % 2 ** 32))


def join_parts(left_part, right_part):
    return (left_part << 32) ^ right_part


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


class GOST_2015:
    def __init__(self, key):

        self.pi = (
            252, 238, 221, 17, 207, 110, 49, 22, 251, 196, 250, 218, 35, 197, 4, 77, 233, 119, 240, 219, 147, 46,
            153, 186, 23, 54, 241, 187, 20, 205, 95, 193, 249, 24, 101, 90, 226, 92, 239, 33, 129, 28, 60, 66,
            139, 1, 142, 79, 5, 132, 2, 174, 227, 106, 143, 160, 6, 11, 237, 152, 127, 212, 211, 31, 235, 52, 44,
            81, 234, 200, 72, 171, 242, 42, 104, 162, 253, 58, 206, 204, 181, 112, 14, 86, 8, 12, 118, 18, 191,
            114, 19, 71, 156, 183, 93, 135, 21, 161, 150, 41, 16, 123, 154, 199, 243, 145, 120, 111, 157, 158,
            178, 177, 50, 117, 25, 61, 255, 53, 138, 126, 109, 84, 198, 128, 195, 189, 13, 87, 223, 245, 36, 169,
            62, 168, 67, 201, 215, 121, 214, 246, 124, 34, 185, 3, 224, 15, 236, 222, 122, 148, 176, 188, 220,
            232, 40, 80, 78, 51, 10, 74, 167, 151, 96, 115, 30, 0, 98, 68, 26, 184, 56, 130, 100, 159, 38, 65,
            173, 69, 70, 146, 39, 94, 85, 47, 140, 163, 165, 125, 105, 213, 149, 59, 7, 88, 179, 64, 134, 172,
            29, 247, 48, 55, 107, 228, 136, 217, 231, 137, 225, 27, 131, 73, 76, 63, 248, 254, 141, 83, 170, 144,
            202, 216, 133, 97, 32, 113, 103, 164, 45, 43, 9, 91, 203, 155, 37, 208, 190, 229, 108, 82, 89, 166,
            116, 210, 230, 244, 180, 192, 209, 102, 175, 194, 57, 75, 99, 182)

        self.pi_inv = (
            165, 45, 50, 143, 14, 48, 56, 192, 84, 230, 158, 57, 85, 126, 82, 145, 100, 3, 87, 90, 28, 96, 7,
            24, 33, 114, 168, 209, 41, 198, 164, 63, 224, 39, 141, 12, 130, 234, 174, 180, 154, 99, 73, 229,
            66, 228, 21, 183, 200, 6, 112, 157, 65, 117, 25, 201, 170, 252, 77, 191, 42, 115, 132, 213, 195,
            175, 43, 134, 167, 177, 178, 91, 70, 211, 159, 253, 212, 15, 156, 47, 155, 67, 239, 217, 121,
            182, 83, 127, 193, 240, 35, 231, 37, 94, 181, 30, 162, 223, 166, 254, 172, 34, 249, 226, 74, 188, 53,
            202, 238, 120, 5, 107, 81, 225, 89, 163, 242, 113, 86, 17, 106, 137, 148, 101, 140, 187, 119, 60,
            123, 40, 171, 210, 49, 222, 196, 95, 204, 207, 118, 44, 184, 216, 46, 54, 219, 105, 179, 20, 149,
            190, 98, 161, 59, 22, 102, 233, 92, 108, 109, 173, 55, 97, 75, 185, 227, 186, 241, 160, 133, 131,
            218, 71, 197, 176, 51, 250, 150, 111, 110, 194, 246, 80, 255, 93, 169, 142, 23, 27, 151, 125,
            236, 88, 247, 31, 251, 124, 9, 13, 122, 103, 69, 135, 220, 232, 79, 29, 78, 4, 235, 248, 243, 62, 61,
            189, 138, 136, 221, 205, 11, 19, 152, 2, 147, 128, 144, 208, 36, 52, 203, 237, 244, 206, 153, 16,
            68, 64, 146, 58, 1, 38, 18, 26, 72, 104, 245, 129, 139, 199, 214, 32, 10, 8, 0, 76, 215, 116)

        # Precomputed table with multiplication results in field x^8 + x^7 + x^6 + x + 1
        f = open(dirname(__file__) + '/gost_tables', 'rb')
        self.multtable = pickle.load(f)
        f.close()

        self.C = [
            [110, 162, 118, 114, 108, 72, 122, 184, 93, 39, 189, 16, 221, 132, 148, 1],
            [220, 135, 236, 228, 216, 144, 244, 179, 186, 78, 185, 32, 121, 203, 235, 2],
            [178, 37, 154, 150, 180, 216, 142, 11, 231, 105, 4, 48, 164, 79, 127, 3],
            [123, 205, 27, 11, 115, 227, 43, 165, 183, 156, 177, 64, 242, 85, 21, 4],
            [21, 111, 109, 121, 31, 171, 81, 29, 234, 187, 12, 80, 47, 209, 129, 5],
            [167, 74, 247, 239, 171, 115, 223, 22, 13, 210, 8, 96, 139, 158, 254, 6],
            [201, 232, 129, 157, 199, 59, 165, 174, 80, 245, 181, 112, 86, 26, 106, 7],
            [246, 89, 54, 22, 230, 5, 86, 137, 173, 251, 161, 128, 39, 170, 42, 8],
            [152, 251, 64, 100, 138, 77, 44, 49, 240, 220, 28, 144, 250, 46, 190, 9],
            [42, 222, 218, 242, 62, 149, 162, 58, 23, 181, 24, 160, 94, 97, 193, 10],
            [68, 124, 172, 128, 82, 221, 216, 130, 74, 146, 165, 176, 131, 229, 85, 11],
            [141, 148, 45, 29, 149, 230, 125, 44, 26, 103, 16, 192, 213, 255, 63, 12],
            [227, 54, 91, 111, 249, 174, 7, 148, 71, 64, 173, 208, 8, 123, 171, 13],
            [81, 19, 193, 249, 77, 118, 137, 159, 160, 41, 169, 224, 172, 52, 212, 14],
            [63, 177, 183, 139, 33, 62, 243, 39, 253, 14, 20, 240, 113, 176, 64, 15],
            [47, 178, 108, 44, 15, 10, 172, 209, 153, 53, 129, 195, 78, 151, 84, 16],
            [65, 16, 26, 94, 99, 66, 214, 105, 196, 18, 60, 211, 147, 19, 192, 17],
            [243, 53, 128, 200, 215, 154, 88, 98, 35, 123, 56, 227, 55, 92, 191, 18],
            [157, 151, 246, 186, 187, 210, 34, 218, 126, 92, 133, 243, 234, 216, 43, 19],
            [84, 127, 119, 39, 124, 233, 135, 116, 46, 169, 48, 131, 188, 194, 65, 20],
            [58, 221, 1, 85, 16, 161, 253, 204, 115, 142, 141, 147, 97, 70, 213, 21],
            [136, 248, 155, 195, 164, 121, 115, 199, 148, 231, 137, 163, 197, 9, 170, 22],
            [230, 90, 237, 177, 200, 49, 9, 127, 201, 192, 52, 179, 24, 141, 62, 23],
            [217, 235, 90, 58, 233, 15, 250, 88, 52, 206, 32, 67, 105, 61, 126, 24],
            [183, 73, 44, 72, 133, 71, 128, 224, 105, 233, 157, 83, 180, 185, 234, 25],
            [5, 108, 182, 222, 49, 159, 14, 235, 142, 128, 153, 99, 16, 246, 149, 26],
            [107, 206, 192, 172, 93, 215, 116, 83, 211, 167, 36, 115, 205, 114, 1, 27],
            [162, 38, 65, 49, 154, 236, 209, 253, 131, 82, 145, 3, 155, 104, 107, 28],
            [204, 132, 55, 67, 246, 164, 171, 69, 222, 117, 44, 19, 70, 236, 255, 29],
            [126, 161, 173, 213, 66, 124, 37, 78, 57, 28, 40, 35, 226, 163, 128, 30],
            [16, 3, 219, 167, 46, 52, 95, 246, 100, 59, 149, 51, 63, 39, 20, 31],
            [94, 167, 216, 88, 30, 20, 155, 97, 241, 106, 193, 69, 156, 237, 168, 32]]

        self.round_key = [key[:16], key[16:]]
        self.round_key = self.round_key + self.key_schedule(self.round_key)

    def sum_field(self, x):
        s = 0
        for a in x:
            s ^= a
        return s

    def x_transformation(self, x, k):
        return [x[i] ^ k[i] for i in range(len(k))]

    def pi_transformation(self, x):
        return self.pi[x]

    def pi_inv_transformation(self, x):
        return self.pi_inv[x]

    def s_transformation(self, x):
        return [self.pi_transformation(x[i]) for i in range(len(x))]

    def s_inv_transformation(self, x):
        return [self.pi_inv_transformation(i) for i in x]

    def l(self, x):
        consts = [148, 32, 133, 16, 194, 192, 1, 251, 1, 192, 194, 16, 133, 32, 148, 1]
        multiplication = [self.multtable[x[i]][consts[i]] for i in range(len(x))]
        return self.sum_field(multiplication)

    def r_transformation(self, x):
        return [self.l(x), ] + x[:-1]

    def r_inv_transformation(self, x):
        return x[1:] + [self.l(x[1:] + [x[0], ]), ]

    def l_transformation(self, x):
        for _ in range(len(x)):
            x = self.r_transformation(x)
        return x

    def l_inv_transformation(self, x):
        for _ in range(len(x)):
            x = self.r_inv_transformation(x)
        return x

    def f_transformation(self, k, a):
        tmp = self.x_transformation(k, a[0])
        tmp = self.s_transformation(tmp)
        tmp = self.l_transformation(tmp)
        tmp = self.x_transformation(tmp, a[1])
        return [tmp, a[0]]

    def key_schedule(self, round_key):
        round_keys = []
        for i in range(4):
            for k in range(8):
                round_key = self.f_transformation(self.C[8 * i + k], round_key)
            round_keys.append(round_key[0])
            round_keys.append(round_key[1])
        return round_keys

    def encryption(self, m):
        for i in range(9):
            m = self.x_transformation(m, self.round_key[i])
            m = self.s_transformation(m)
            m = self.l_transformation(m)
        m = self.x_transformation(m, self.round_key[9])
        return m

    def decryption(self, c):
        for i in range(9, 0, -1):
            c = self.x_transformation(c, self.round_key[i])
            c = self.l_inv_transformation(c)
            c = self.s_inv_transformation(c)
        c = self.x_transformation(c, self.round_key[0])
        return c


def GOST_R_2015_M_test(operation, key):

    if operation == 1:
        text = int('fedcba9876543210', 16)
        (left_part, right_part) = text >> 32, text & 2 ** 32 - 1
        for i in range(31):
            (left_part, right_part) = (right_part, left_part ^ g(right_part, key[i]))
        print(format(join_parts(left_part ^ g(right_part, key[-1]), right_part), '0x'))

    if operation == 2:
        text = int('4ee901e5c2d8ca3d', 16)
        key.reverse()
        left_part, right_part = text >> 32, text & 2 ** 32 - 1
        for j in range(31):
            (left_part, right_part) = (right_part, left_part ^ g(right_part, key[j]))
        print(format(join_parts(left_part ^ g(right_part, key[-1]), right_part), "0x"))


def GOST_R_2015_K_test():
    text = list(binascii.unhexlify('1122334455667700ffeeddccbbaa9988'))
    key = list(binascii.unhexlify('8899aabbccddeeff0011223344556677fedcba98765432100123456789abcdef'))
    test = GOST_2015(key)
    enc = test.encryption(text)
    dec = test.decryption(enc)
    print("Encrypted text: ", binascii.hexlify(bytearray(enc)))
    print("Decrypted text: ", binascii.hexlify(bytearray(dec)))


def GOST_R_2015_M(operation, text):
    """
    key = input('Enter a key: ')
    if len(key) != 64:
        print("Wrong key!")
        exit()
    """
    key = magma_key_schedule(int('ffeeddccbbaa99887766554433221100f0f1f2f3f4f5f6f7f8f9fafbfcfdfeff', 16))
    print("""Enter mode:
                1.  GOST
                2.  TEXT
        """)
    mode = int(input())

    if mode == 1:
        GOST_R_2015_M_test(operation, key)

    else:
        if operation == 1:

            ciphertext = ''

            while len(text) > 0:

                if len(text) < 4:
                    for _ in range(4 - len(text)):
                        text += str(list_alph[random.randint(0, 31)])

                text_16 = int(text[:4].encode('utf-8').hex(), 16)

                left_part, right_part = text_16 >> 32, text_16 & 2 ** 32 - 1

                for i in range(31):
                    (left_part, right_part) = (right_part, left_part ^ g(right_part, key[i]))
                ciphertext += str(hex(join_parts(left_part ^ g(right_part, key[-1]), right_part)))[2:] + " "

                text = text[4:]

            print("Encrypted text: ", ciphertext)

        if operation == 2:

            key.reverse()
            res = ''
            text = text.split()
            text = [int(h, 16) for h in text]

            for i in text:

                left_part, right_part = i >> 32, i & 2 ** 32 - 1

                for j in range(31):
                    (left_part, right_part) = (right_part, left_part ^ g(right_part, key[j]))

                result = format(join_parts(left_part ^ g(right_part, key[-1]), right_part), 'x')
                res += bytes.fromhex(result).decode('utf-8')

            answer = decryption_format(str(res))

            print("Decrypted text: ", answer[:(answer.rfind('.')) + 1])
            print()


def GOST_R_2015_K(operation, text):
    print("""Enter mode:
                    1.  GOST
                    2.  TEXT
            """)
    mode = int(input())

    if mode == 1:
        GOST_R_2015_K_test()

    else:
        """
        key = list(binascii.unhexlify(input('Enter a key: ')))
        if len(key) != 32:
            print("Length of key should be = 64!")
            exit()
        """
        key = list(binascii.unhexlify('8899aabbccddeeff0011223344556677fedcba98765432100123456789abcdef'))
        a = GOST_2015(key)
        result = ''
        if operation == 1:

            while len(text) > 0:
                ascii_text = []
                for i in range(16 if len(text) >= 16 else len(text)):
                    ascii_text.append(ord(text[i].encode('windows-1251')))

                if len(ascii_text) < 16:
                    for _ in range(16 - len(ascii_text)):
                        ascii_text.append(random.randint(224, 255))

                enc = a.encryption(ascii_text)
                result += str(binascii.hexlify(bytearray(enc)))[2: -1]

                text = text[16:]

            print("Encrypted text: ", result)

        if operation == 2:
            for _ in range(len(text) // 32):
                dec = a.decryption(binascii.unhexlify(text[:32]))
                result += bytes(dec).decode('windows-1251')
                text = text[32:]

            answer = decryption_format(result)
            print("Decrypted text: ", answer[:(answer.rfind('.')) + 1])


import sys
while True:

    print("""Select a cipher: 
             1.  МАГМА
             2.  Кузнечик
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

    if select == 1:
        GOST_R_2015_M(operation, text.lower())
        print()

    if select == 2:
        GOST_R_2015_K(operation, text.lower())
        print()
