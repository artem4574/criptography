from block_A_simple_replacement_ciphers import decryption_format


def generate_alph_matrix(string_alph):

    alphabet = [[0]*len(string_alph) for _ in range(len(string_alph))]

    for i in range(len(string_alph)):
        for j in range(len(string_alph)):
            alphabet[i][j] = (string_alph[j+i-len(string_alph)])

    return alphabet


def Trithemius_cipher(operation, text):
    
    alph = generate_alph_matrix('абвгдежзийклмнопрстуфхцчшщъыьэюя')
    answer = ''

    if operation == 1:        

        for i in range(len(text)):
            answer += alph[i % 32][alph[0].index(text[i])]

        print("Encrypted text: ", ' '.join(answer[i: i + 5] for i in range(0, len(answer), 5)))
        print()
 
    if operation == 2:

        for i in range(len(text)):
            answer += alph[0][alph[i % 32].index(text[i])]

        result = decryption_format(answer)

        print("Decrypted text: ", result)
        print()


def Belazo_cipher(operation, text):
    
    key: str = str(input('Enter keyword:'))
    if len(key) > len(text) or len(key) < 2:
        print("Length of key should be < than length of text and > than 1!")
        exit()

    alph = generate_alph_matrix('абвгдежзийклмнопрстуфхцчшщъыьэюя')
    answer = ''

    if operation == 1:

        for i in range(len(text)):
            answer += alph[alph[0].index(key[i % len(key)])][alph[0].index(text[i])]

        print("Encrypted text: ", ' '.join(answer[i: i + 5] for i in range(0, len(answer), 5)))
        print()

    if operation == 2:          
        for i in range(len(text)):
            answer += alph[0][alph[alph[0].index(key[i % len(key)])].index(text[i])]

        result = decryption_format(answer)

        print("Decrypted text: ", result)
        print()


def Vigenere(operation, text):
   
    key: str = str(input('Enter key: '))
    if len(key) != 1:
        print("Length of key should be = 1!")
        exit()

    alph = generate_alph_matrix('абвгдежзийклмнопрстуфхцчшщъыьэюя')
    answer = ''

    if operation == 1:

        key += text[:-1]
        for i in range(len(text)):
            answer += alph[alph[0].index(key[i])][alph[0].index(text[i])]

        print("Encrypted text: ", ' '.join(answer[i: i+5] for i in range(0, len(answer), 5)))
        print()

    if operation == 2:

        for i in range(len(text)):
            answer += alph[alph[alph[0].index(key[i % len(key)])].index(text[i])][0]
            key += answer[i]
        
        result = decryption_format(answer)

        print("Decrypted text: ", result)
        print()


def Vigenere_2(text, operation, answer=""):
    
    key: str = str(input('Enter key: '))
    alph = generate_alph_matrix('абвгдежзийклмнопрстуфхцчшщъыьэюя')

    if operation == 1:          

        for i in range(len(text)):
            answer += alph[alph[0].index(key[i])][alph[0].index(text[i])]
            key += answer[i]

        print("Encrypted text: ", ' '.join(answer[i: i + 5] for i in range(0, len(answer), 5)))
        print()

    if operation == 2:

        for i in range(len(text)):
            answer += alph[alph[alph[0].index(key[i % len(key)])].index(text[i])][0]
            key += text[i]
        
        result = decryption_format(answer)

        print("Decrypted text: ", result)
        print()


'''
import sys
while True:

    print("""Select a cipher: 
             1.  Trithemius
             2.  Belazo
             3.  Vigenere
             4.  Vigenere 2
             5.  Exit
         """)
    select: int = int(input())
    if select == 5: 
        sys.exit()

    if select not in [1, 2, 3, 4, 5]:
        print("Wrong select!")
        continue

    print(""" Select an action: 
                1. Encryption 
                2. Decryption""")
    operation: int = int(input())

    text: str = str(input('Enter text: '))
    print()

    if operation == 1:
        for i in range(len(text)):
            if text.find('.') != -1:
                index = text.find('.')
                str1_split1 = text[:index]
                str1_split2 = text[index+1:]
                text = str1_split1 + 'тчк' + str1_split2
            if text.find(',') != -1:
                index = text.find(',')
                str1_split1 = text[:index]
                str1_split2 = text[index+1:]
                text = str1_split1 + 'зпт' + str1_split2
            if text.find(' ') != -1:
                index = text.find(' ')
                str1_split1 = text[:index]
                str1_split2 = text[index+1:]
                text = str1_split1 + 'прб' + str1_split2
            
    else: text = text.replace(' ', '')

    if select == 1: 
        Trithemius_cipher(text.lower(), operation)
        print()

    if select == 2: 
        Belazo_cipher(text.lower(), operation)
        print()

    if select == 3: 
        Vigenere(text.lower(), operation)
        print()
    
    if select == 4: 
        Vigenere_2(text.lower(), operation)
        print()
'''