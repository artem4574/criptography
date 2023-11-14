import numpy as np

def generate_alph_matrix(string_alph):
    alphabet = [[0]*len(string_alph) for i in range(len(string_alph))]
    for i in range(len(string_alph)):
        for j in range(len(string_alph)):
            alphabet[i][j] = (string_alph[j+i-len(string_alph)])
            '''print(alphabet[i][j], end='')
        print()'''
    return alphabet


def Trithemius_sipher():
    text: str = str(input('Enter text: '))
    print(""" Select an action: 
                 1. Encryption 
                 2. Decryption""")
    operation: int = int(input())
    result_text, text, k = "", text.replace(' ', ''), 0
    alph = generate_alph_matrix('абвгдежзийклмнопрстуфхцчшщъыьэюя')
    if operation == 1:          #encryption
        for i in range(len(text)): result_text+=alph[i%32][alph[0].index(text[i])]
        print("Encrypted text: ", end=' ')
        for i in result_text:
            print(i, end='')
            k += 1
            if k % 5 == 0: print(" ", end='')
        print()
        exit()
    if operation == 2:          #decryption
        for i in range(len(text)): result_text+=alph[0][alph[i%32].index(text[i])]
        print("Decrypted text: ", end=' ')
        for i in result_text: print(i, end='')
        print()
        exit()
    else:
         print("Error in select!")
         exit()


def Belazo_sipher():
    text: str = str(input('Enter text: '))
    key: str = str(input('Enter keyword(must not contain duplicate letters and start with A): '))
    print(""" Select an action: 
                1. Encryption 
                2. Decryption""")
    operation: int = int(input())
    result_text, text, k = "", text.replace(' ', ''), 0
    alph = generate_alph_matrix('абвгдежзийклмнопрстуфхцчшщъыьэюя')
    if operation==1:           #encryption
        for i in range(len(text)): result_text+=alph[alph[0].index(key[i%len(key)])][alph[0].index(text[i])]
        print("Encrypted text: ", end=' ')
        for i in result_text:
            print(i, end='')
            k += 1
            if k % 5 == 0: print(" ", end='')
        print()
        exit()
    if operation == 2:          #decryption
        for i in range(len(text)): result_text+=alph[0][alph[alph[0].index(key[i%len(key)])].index(text[i])]
        print("Decrypted text: ", end=' ')
        for i in result_text: print(i, end='')
        print()
        exit()
    else:
         print("Error in select!")
         exit()


def Vigenere():
    text: str = str(input('Enter text: '))
    key: str = str(input('Enter key: '))
    print(""" Select an action: 
                 1. Encryption 
                 2. Decryption""")
    operation: int = int(input())
    result_text, text, k = "", text.replace(' ', ''), 0
    alph = generate_alph_matrix('абвгдежзийклмнопрстуфхцчшщъыьэюя')
    if operation == 1:          #encryption
        key += text[:-1]
        for i in range(len(text)): result_text+=alph[alph[0].index(key[i])][alph[0].index(text[i])]
        print("Encrypted text: ", end=' ')
        for i in result_text:
            print(i, end='')
            k += 1
            if k % 5 == 0: print(" ", end='')
        print()
        exit()
    if operation == 2:          #decryption
        for i in range(len(text)):
            result_text+=alph[alph[alph[0].index(key[i%len(key)])].index(text[i])][0]
            key+=result_text[i]
        print("Decrypted text: ", end=' ')
        for i in result_text: print(i, end='')
        print()
        exit()
    else:
         print("Error in select!")
         exit()


def Vigenere_2():
    text: str = str(input('Enter text: '))
    key: str = str(input('Enter key: '))
    print(""" Select an action: 
                 1. Encryption 
                 2. Decryption""")
    operation: int = int(input())
    result_text, text, k = "", text.replace(' ', ''), 0
    alph = generate_alph_matrix('абвгдежзийклмнопрстуфхцчшщъыьэюя')
    if operation == 1:          #encryption
        for i in range(len(text)):
            result_text+=alph[alph[0].index(key[i])][alph[0].index(text[i])]
            key += result_text[i]
        print("Encrypted text: ", end=' ')
        for i in result_text:
            print(i, end='')
            k += 1
            if k % 5 == 0: print(" ", end='')
        print()
        exit()
    if operation == 2:           #decryption
        for i in range(len(text)):
            result_text += alph[alph[alph[0].index(key[i%len(key)])].index(text[i])][0]
            key += text[i]
        print("Decrypted text: ", end=' ')
        for i in result_text: print(i, end='')
        print()
        exit()
    else:
        print("Error in select!")
        exit()