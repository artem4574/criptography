import sys

def generate_alph_matrix(string_alph):
    alphabet = [[0]*len(string_alph) for i in range(len(string_alph))]
    for i in range(len(string_alph)):
        for j in range(len(string_alph)):
            alphabet[i][j] = (string_alph[j+i-len(string_alph)])
            '''print(alphabet[i][j], end='')
        print()'''
    return alphabet


def Trithemius_cipher(text, operation, answer = ""):
    
    alph = generate_alph_matrix('абвгдежзийклмнопрстуфхцчшщъыьэюя')

    if operation == 1:        
        k = 0  
        for i in range(len(text)): answer+=alph[i%32][alph[0].index(text[i])]

        print("Encrypted text: ", end=' ')
        for i in answer:
            print(i, end='')
            k += 1
            if k % 5 == 0: print(" ", end='')
        print()
 
    if operation == 2:          
        for i in range(len(text)): answer+=alph[0][alph[i%32].index(text[i])]

        answer = answer.replace('тчк', '.')
        answer = answer.replace('зпт', ',')

        print("Decrypted text: ", end=' ')
        for i in answer: print(i, end='')
        print()


def Belazo_cipher(text, operation, answer = ""):
    
    key: str = str(input('Enter keyword(must not contain duplicate letters and start with A): '))
    alph = generate_alph_matrix('абвгдежзийклмнопрстуфхцчшщъыьэюя')

    if operation==1:           
        k = 0
        for i in range(len(text)): answer+=alph[alph[0].index(key[i%len(key)])][alph[0].index(text[i])]

        print("Encrypted text: ", end=' ')
        for i in answer:
            print(i, end='')
            k += 1
            if k % 5 == 0: print(" ", end='')
        print()

    if operation == 2:          
        for i in range(len(text)): answer+=alph[0][alph[alph[0].index(key[i%len(key)])].index(text[i])]

        answer = answer.replace('тчк', '.')
        answer = answer.replace('зпт', ',')

        print("Decrypted text: ", end=' ')
        for i in answer: print(i, end='')
        print()


def Vigenere(text, operation, answer = ""):
   
    key: str = str(input('Enter key: '))
    alph = generate_alph_matrix('абвгдежзийклмнопрстуфхцчшщъыьэюя')

    if operation == 1:          
        k = 0
        key += text[:-1]
        for i in range(len(text)): answer+=alph[alph[0].index(key[i])][alph[0].index(text[i])]

        print("Encrypted text: ", end=' ')
        for i in answer:
            print(i, end='')
            k += 1
            if k % 5 == 0: print(" ", end='')
        print()

    if operation == 2:          
        for i in range(len(text)):
            answer+=alph[alph[alph[0].index(key[i%len(key)])].index(text[i])][0]
            key+=answer[i]
        
        answer = answer.replace('тчк', '.')
        answer = answer.replace('зпт', ',')

        print("Decrypted text: ", end=' ')
        for i in answer: print(i, end='')
        print()


def Vigenere_2(text, operation, answer = ""):
    
    key: str = str(input('Enter key: '))
    alph = generate_alph_matrix('абвгдежзийклмнопрстуфхцчшщъыьэюя')
    
    if operation == 1:          
        k = 0
        for i in range(len(text)):
            answer+=alph[alph[0].index(key[i])][alph[0].index(text[i])]
            key += answer[i]

        print("Encrypted text: ", end=' ')
        for i in answer:
            print(i, end='')
            k += 1
            if k % 5 == 0: print(" ", end='')
        print()

    if operation == 2:       

        for i in range(len(text)):
            answer += alph[alph[alph[0].index(key[i%len(key)])].index(text[i])][0]
            key += text[i]
        
        answer = answer.replace('тчк', '.')
        answer = answer.replace('зпт', ',')

        print("Decrypted text: ", end=' ')
        for i in answer: print(i, end='')
        print()

while (True):

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

    if select not in [1,2,3,4,5]: 
        print("Wrong select!")
        continue

    print(""" Select an action: 
                1. Encryption 
                2. Decryption""")
    operation: int = int(input())
    
    text: str = str(input('Enter text: '))
    text_format = str(text.replace(' ', ''))
    for i in range(len(text_format)):
        if text_format.find('.') != -1:
            index = text_format.find('.')
            str1_split1 = text_format[:index]
            str1_split2 = text_format[index+1:]
            text_format = str1_split1 + 'тчк' + str1_split2
        if text_format.find(',') != -1:
            index = text_format.find(',')
            str1_split1 = text_format[:index]
            str1_split2 = text_format[index+1:]
            text_format = str1_split1 + 'зпт' + str1_split2

    if select == 1: 
        Trithemius_cipher(text_format, operation)
        print()

    if select == 2: 
        Belazo_cipher(text_format, operation)
        print()

    if select == 3: 
        Vigenere(text_format, operation)
        print()
    
    if select == 4: 
        Vigenere_2(text_format, operation)
        print()