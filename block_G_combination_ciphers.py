import random
from block_A_simple_replacement_ciphers import decryption_format
from block_A_simple_replacement_ciphers import listalf as list_alph

s_block = [
    [0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76],
    [0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0],
    [0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15],
    [0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75],
    [0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84],
    [0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF],
    [0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8],
    [0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2],
    [0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73],
    [0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB],
    [0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79],
    [0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08],
    [0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A],
    [0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E],
    [0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF],
    [0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16]]

inv_s_block = [
    [0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB],
    [0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB],
    [0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E],
    [0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25],
    [0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92],
    [0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84],
    [0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06],
    [0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B],
    [0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73],
    [0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E],
    [0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B],
    [0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4],
    [0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F],
    [0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF],
    [0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61],
    [0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D]]

Rcon = [0x01000000, 0x02000000, 0x04000000, 0x08000000, 0x10000000,
        0x20000000, 0x40000000, 0x80000000, 0x1b000000, 0x36000000]

pi = [[12, 4, 6, 2, 10, 5, 11, 9, 14, 8, 13, 7, 0, 3, 15, 1],
      [6, 8, 2, 3, 9, 10, 5, 12, 1, 14, 4, 7, 11, 13, 0, 15],
      [11, 3, 5, 8, 2, 15, 10, 13, 14, 1, 7, 4, 12, 9, 6, 0],
      [12, 8, 2, 1, 13, 4, 15, 6, 7, 0, 10, 5, 3, 14, 9, 11],
      [7, 15, 5, 10, 8, 1, 6, 13, 0, 9, 3, 14, 11, 4, 2, 12],
      [5, 13, 15, 6, 9, 2, 12, 10, 11, 7, 8, 1, 4, 3, 14, 0],
      [8, 14, 2, 5, 6, 9, 1, 12, 15, 4, 11, 0, 13, 10, 3, 7],
      [1, 7, 14, 13, 0, 5, 8, 3, 4, 15, 10, 6, 9, 12, 11, 2]]


def word_rot(x):
    return ((x << 8) | (x >> 24)) & 0xffffffff


def sub_word(x):
    temp = 0
    temp = (temp << 8) | s_block[(x >> 28) & 0x0f][(x >> 24) & 0x0f]
    temp = (temp << 8) | s_block[(x >> 20) & 0x0f][(x >> 16) & 0x0f]
    temp = (temp << 8) | s_block[(x >> 12) & 0x0f][(x >> 8) & 0x0f]
    temp = (temp << 8) | s_block[(x >> 4) & 0x0f][(x >> 0) & 0x0f]
    return temp


def AddRoundKey(state, ikey):
    result = []

    for i in range(4):
        for j in range(4):
            result.append((state[4 * i + j] ^ ((ikey[j] << 8 * i) >> 24)) & 0xff)

    return bytes(result)


def sub_bytes(state):
    sub = []
    for i in state:
        sub.append(s_block[i >> 4][i & 0x0f])
    return bytes(sub)


def shift_rows(state):
    shift = b''
    shift += state[0:4] + state[5:8] + state[4:5] + state[10:12] + state[8:10] + state[15:16] + state[12:15]
    return shift


def GFMul(a, b):
    p, hi_bit_set = 0, 0

    for _ in range(8):
        if b & 1 != 0:
            p ^= a
        hi_bit_set = a & 0x80
        a = (a << 1) & 0xff
        if hi_bit_set != 0:
            a ^= 0x1b  # x^8 + x^4 + x^3 + x + 1
        b >>= 1

    return p & 0xff


def mix_columns(state):
    mix_state = [0] * 16

    for i in range(4):
        arr = []
        for j in range(4):
            arr.append(state[i + j * 4])

        mix_state[i] = GFMul(0x02, arr[0]) ^ GFMul(0x03, arr[1]) ^ arr[2] ^ arr[3]
        mix_state[i + 4] = arr[0] ^ GFMul(0x02, arr[1]) ^ GFMul(0x03, arr[2]) ^ arr[3]
        mix_state[i + 8] = arr[0] ^ arr[1] ^ GFMul(0x02, arr[2]) ^ GFMul(0x03, arr[3])
        mix_state[i + 12] = GFMul(0x03, arr[0]) ^ arr[1] ^ arr[2] ^ GFMul(0x02, arr[3])

    return bytes(mix_state)


def inv_shift_rows(state):
    inv_shift = b''
    inv_shift += state[0:4] + state[7:8] + state[4:7] + state[10:12] + state[8:10] + state[13:16] + state[12:13]
    return inv_shift


def inv_sub_bytes(state):
    inv_sub = []
    for i in state:
        inv_sub.append(inv_s_block[i >> 4][i & 0x0f])
    return bytes(inv_sub)


def inv_mix_columns(state):
    inv_mix = [0] * 16

    for i in range(4):
        arr = []
        for j in range(4):
            arr.append(state[i + j * 4])

        inv_mix[i] = GFMul(0x0e, arr[0]) ^ GFMul(0x0b, arr[1]) ^ GFMul(0x0d, arr[2]) ^ GFMul(0x09, arr[3])
        inv_mix[i + 4] = GFMul(0x09, arr[0]) ^ GFMul(0x0e, arr[1]) ^ GFMul(0x0b, arr[2]) ^ GFMul(0x0d, arr[3])
        inv_mix[i + 8] = GFMul(0x0d, arr[0]) ^ GFMul(0x09, arr[1]) ^ GFMul(0x0e, arr[2]) ^ GFMul(0x0b, arr[3])
        inv_mix[i + 12] = GFMul(0x0b, arr[0]) ^ GFMul(0x0d, arr[1]) ^ GFMul(0x09, arr[2]) ^ GFMul(0x0e, arr[3])

    return bytes(inv_mix)


class AES(object):
    def __init__(self, K: bytes):
        self.Nk, self.Nb, self.Nr = 4, 4, 10
        self.K = K[:self.Nk * 8]

        while len(self.K) < self.Nk * 8:
            self.K += b'\x00'
        self.exp = self.key_expansion()

    def Encrypt(self, b_text: bytes) -> bytes:

        while len(b_text) % 16 != 0:
            b_text += b'\x00'

        ciphertext = b''

        for i in range(len(b_text) // 16):
            state = b_text[i * 16:i * 16 + 16]
            ikey = self.exp[:4]
            state = AddRoundKey(state, ikey)

            for round in range(1, self.Nr):
                state = sub_bytes(state)
                state = shift_rows(state)
                state = mix_columns(state)
                ikey = self.exp[4 * round:4 * round + 4]
                state = AddRoundKey(state, ikey)

            state = sub_bytes(state)
            state = shift_rows(state)
            ikey = self.exp[4 * self.Nr:]
            state = AddRoundKey(state, ikey)
            ciphertext += state

        return ciphertext

    def Decrypt(self, b_text: bytes) -> bytes:
        dec_text = b''

        for i in range(len(b_text) // 16):
            state = b_text[i * 16:i * 16 + 16]
            ikey = self.exp[self.Nr * 4:]
            state = AddRoundKey(state, ikey)

            for round in range(self.Nr - 1, 0, -1):

                state = inv_shift_rows(state)
                state = inv_sub_bytes(state)
                ikey = self.exp[4 * round:4 * round + 4]
                state = AddRoundKey(state, ikey)
                state = inv_mix_columns(state)

            state = inv_shift_rows(state)
            state = inv_sub_bytes(state)
            ikey = self.exp[:4]
            state = AddRoundKey(state, ikey)
            dec_text += state

        return dec_text

    def key_expansion(self):

        exp = []

        for i in range(self.Nk):
            temp = 0
            for j in range(4):
                temp = (temp << 8) | self.K[4 * i + j]
            exp.append(temp)

        for i in range(self.Nk, self.Nb * (self.Nr + 1)):
            temp = exp[i - 1]

            if i % self.Nk == 0:
                temp = sub_word(word_rot(temp)) ^ Rcon[i // self.Nk - 1]

            elif self.Nk > 6 and i % self.Nk == 4:
                temp = sub_word(temp)

            exp.append(exp[i - self.Nk] ^ temp)

        return exp


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


def aes(operation, text):

    key = b'000102030405060708090a0b0c0d0e0f'
    a = AES(key)

    if operation == 1:

        encrypted_text = a.Encrypt(text.encode('utf-8'))

        print("Encrypted text: ", end='')
        for i in encrypted_text:
            print(hex(i)[2:].rjust(2, '0'), end='')

    if operation == 2:

        decrypted_text = a.Decrypt(bytes.fromhex(text))

        answer = decryption_format(decrypted_text.decode('utf-8'))
        print("Decrypted text: ", answer)


def magma(operation, text):

    keys = magma_key_schedule(int(input('Enter a 256-bit key: '), 16))

    # keys = magma_key_schedule(int('ffeeddccbbaa99887766554433221100f0f1f2f3f4f5f6f7f8f9fafbfcfdfeff', 16))

    if operation == 1:
        ciphertext = ''

        while len(text) > 0:

            if len(text) < 4:
                for i in range(4 - len(text)):
                    text += str(list_alph[random.randint(0, 31)])

            text_16 = int(text[:4].encode('utf-8').hex(), 16)

            left_part, right_part = text_16 >> 32, text_16 & 2 ** 32 - 1

            for i in range(31):
                (left_part, right_part) = (right_part, left_part ^ g(right_part, keys[i]))
            ciphertext += str(hex(join_parts(left_part ^ g(right_part, keys[-1]), right_part)))[2:] + " "

            text = text[4:]

        print("Encrypted text: ", ciphertext)

    if operation == 2:

        keys.reverse()
        res = ''
        text = text.split()
        text = [int(h, 16) for h in text]

        for i in text:

            left_part, right_part = i >> 32, i & 2 ** 32 - 1

            for j in range(31):
                (left_part, right_part) = (right_part, left_part ^ g(right_part, keys[j]))

            result = format(join_parts(left_part ^ g(right_part, keys[-1]), right_part), 'x')
            res += bytes.fromhex(result).decode('utf-8')

        answer = decryption_format(str(res))

        print("Decrypted text: ", answer[:(answer.rfind('.')) + 1])
        print()


'''
import sys
while True:

    print("""Select a cipher: 
             1.  МАГМА
             2.  AES
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
        magma(operation, text.lower())
        print()

    if select == 2:
        aes(operation, text.lower())
        print()
'''