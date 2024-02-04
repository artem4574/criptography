from itertools import zip_longest
import numpy

listalf = ["а", "б", "в", "г", "д", "е", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]

#РЛСЛОС
def xor(scr, register):
    for_xor_scr = [] #массив единиц scrambler
    for_xor_reg = [] #массив регистра
    boofer = []      #буфер битов для xor
    for i in range(len(scr)): for_xor_scr.append(int(scr[i]))
    for i in range(len(register)): for_xor_reg.append(int(register[i]))
    for i in range(len(scr)):
        if for_xor_scr[i] == 1: boofer.append(for_xor_reg[i])
    return str(numpy.bitwise_xor.reduce(boofer)) + register[:-1]


def grouper(n, iterable, fillvalue = None):
    args = [iter(iterable)] * n
    return zip_longest(fillvalue=fillvalue, *args)


def digitization(open_text):
    dig_text = ""
    for i in range(len(open_text)):
        shiphr = (listalf.index(open_text[i]))
        shiphr = int((shiphr)) + 1
        dig_text += (format(shiphr, '06b'))
    return dig_text


def undigitization(d_text):
    d_text = ' '.join(''.join(g) for g in grouper(6, d_text, ''))
    d_array = d_text.split()
    open_text = ""
    for i in d_array: print(i, " ", end='')
    for i in d_array:
        open_text += (listalf[int(str(int(i)), 2) - 1])
        #print(int(str(int(i)), 2), " ", end='')
    return open_text


def gamming(text, reg1, reg2, scrambler1, scrambler2):
    result_str = ""
    for i in range(len(text)):
        ex_bit1 = reg1[len(reg1) - 1]
        ex_bit2 = reg2[len(reg2) - 1]
        code_bit = int(ex_bit1)^int(ex_bit2)
        res_bit = int(text[i])^code_bit
        result_str += str(res_bit)
        print(reg1, " ", ex_bit1, " ", reg2, " ", ex_bit2, " ", code_bit, " ", text[i], " ", res_bit)
        reg1 = xor(scrambler1, reg1)
        reg2 = xor(scrambler2, reg2)
    return result_str


scrambler1: str = str(input('Enter scrambler_1: '))
scrambler2: str = str(input('Enter scrambler_2: '))
reg1: str = str(input('Enter key_1: '))
reg2: str = str(input('Enter key_2: '))
print(""" Select an action: 
    1. Encryption 
    2. Decryption""")
choose: int = int(input())
if choose == 1:
    open_text: str = str(input('Enter open text: '))
    d_text = digitization(open_text)
    result_str = gamming(d_text, reg1, reg2, scrambler1, scrambler2)
    print("Cipher text:")
    result_str = ' '.join(''.join(g) for g in grouper(5, result_str, ''))
    result_array = result_str.split()
    for i in range(len(result_array)):
        print(result_array[i], " ", end = '')
        if i % 15 == 14: print()
    exit()
if choose == 2:
    ciphertext: str = str(input('Enter ciphertext: '))
    dig_text = gamming((ciphertext.replace(' ', '')), reg1, reg2, scrambler1, scrambler2)
    print("Decrypted text: ", undigitization(dig_text))
    exit()
else:
    print("Error in select!")
    exit()


#scrambler1 = 10110
#scrambler2 = 1001
#key1 = 10110
#key2 = 1001
#open text = одиндуракможетбольшеспрашиватьзптчемдесятьумныхответитьтчк
#dig_text = 001111000101001001001110000101010100010001000001001011001101001111000111000110010011000010001111001100011101011001000110010010010000010001000001011001001001000011000001010011011101001000010000010011011000000110001101000101000110010010100000010011011101010100001101001110011100010110001111010011000011000110010011001001010011011101010011011000001011
#encrypted text = 11000  01000  01101  10011  10111  10111  11110  11100  10101  00100  00111  11011  00110  11001  11001 00010  01010  10110  01100  00011  01100  00011  00000  00011  00111  11000  01010  10100  01111  10100  11000  11010  10011  00110  00100  00100  10001  00101  01000  10111  00101  00101  10111  00101  10010  11111  01011  11110  11010  01001  01000  11000  11001  01110  01100  11110  11111  10010  00011  11100   01001  01101  00001  01001  10000  01101  10111  10110  10010  000
    
# Shannon's notebook
    
def digitization(open_text, result = []):
    for i in range(len(open_text)): result.append(listalf.index(open_text[i])+1)
    return result


def undigitization(ciphertext, result = []):
    for i in range(len(ciphertext)): result.append(listalf[ciphertext[i]-1])
    return result


def encrypt_text(text, gamma, encrypted_text = []):
    for i in range(len(text)): 
        encrypted_text.append((text[i] + gamma[i]) % 32)
        print(text[i], gamma[i])
    return encrypted_text


def decrypt_text(text, gamma):
    dec_text = [0]*len(text)
    for i in range(len(text)):
        if gamma[i] < text[i]: dec_text[i] = text[i] - gamma[i]
        else: dec_text[i] = text[i] + 32 - gamma[i]
    return dec_text


def generate_gamma(a, c, t0, length):
    t, gamma = t0, []
    for i in range(length+1):
        gamma.append((a * t + c) % 32)
        t = (a * t + c) % 32
    return gamma


def main():
    a, c, t0, k = int(input("Enter the value of a (a % 4 = 1): ")), int(input("Enter the value of c (с % 2 != 0): ")) % 32, int(input("Enter the value of T0: ")), 0
    print(""" Select an action: 
        1. Encryption 
        2. Decryption""")
    choose: int = int(input())
    if choose == 1:
       # open_text = str(input("Enter open text: "))
        open_text = 'одинчасутромстоитдвухчасоввечеромтчк'
        ciphertext = undigitization(encrypt_text(digitization((open_text.replace(' ', ''))), generate_gamma(a, c, t0, len(open_text))))
        print("Encrypted text: ", end=' ')
        for i in ciphertext:
            print(i, end='')
            k += 1
            if k%5 == 0: print(" ", end='')
        print()
    if choose == 2:
        ciphertext = str(input("Enter ciphertext: "))
        dec_text = undigitization(decrypt_text(digitization(ciphertext.replace(' ', '')), generate_gamma(a, c, t0, len(ciphertext.replace(' ', '')))))
        print("Decrypted text: ", end='')
        for i in dec_text:
            print(i, end='')


if __name__ == "__main__":
    main()