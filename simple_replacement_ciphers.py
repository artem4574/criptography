import sys
listalf = ["а", "б", "в", "г", "д", "е", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
hard_dictionary = {
    "а":"11", "б":"12", "в":"13", "г":"14", "д":"15", "е":"16",
    "ж":"21", "з":"22", "и":"23", "й":"24", "к":"25", "л":"26", 
    "м":"31", "н":"32", "о":"33", "п":"34", "р":"35", "с":"36", 
    "т":"41", "у":"42", "ф":"43", "х":"44", "ц":"45", "ч":"46", 
    "ш":"51", "щ":"52", "ъ":"53", "ы":"54", "ь":"55", "э":"56", 
    "ю":"61", "я":"62"}


def Caesar(result_text, operation, answer = ""):
    
    shift: int = int(input('Enter shift: '))
    if (shift % len(listalf) == 0 or shift == 0):
        print("Wrong shift!")
        exit()
   
    if (operation == 1):
        k = 0
        for i in range(len(result_text)): answer += (listalf[(listalf.index(result_text[i]) + shift) % 32])
        print("Encrypted text: ", end=' ')
        for i in answer:
            print(i, end='')
            k += 1
            if k % 5 == 0: print(" ", end='')
        print()
    else:
        for i in range(len(result_text)): answer += (listalf[(listalf.index(result_text[i]) - shift) % 32])
        answer = answer.replace('тчк', '.')
        answer = answer.replace('зпт', ',')
        print("Decrypted text: ", end=' ')
        for i in answer:
            print(i, end='')
    
    
def ATBASH(result_text, answer = ""):

    for i in range(len(result_text)): answer += (listalf[-listalf.index(result_text[i])-1])

    answer = answer.replace('тчк', '.')
    answer = answer.replace('зпт', ',')

    print("Encrypted/decrypted text: ", end=' ')
    for i in answer:
        print(i, end='')
        '''k += 1
        if k % 5 == 0: print(" ", end='')'''
    print()

def Polybi_square(result_text, operation, answer = ""):
    
    if (operation==1):
        k = 0
        for x in result_text: answer += hard_dictionary.get(x)
        print("Encrypted text: ", end=' ')
        for i in answer:
            print(i, end='')
            k += 1
            if k % 5 == 0: print(" ", end='')
        print()
    else:
        list_fraze, step = [], 2
        for i in range(0, len(result_text), 2):
            list_fraze.append(result_text[i:step])
            step += 2
        key_hard_dictionary_list = list(hard_dictionary.keys())
        val_hard_dictionary_list = list(hard_dictionary.values())
        for x in list_fraze: answer += key_hard_dictionary_list[val_hard_dictionary_list.index(x)]

        answer = answer.replace('тчк', '.')
        answer = answer.replace('зпт', ',')

        print("Decrypted text: ", end=' ')
        for i in answer:
            print(i, end='')
        print()


while (True):

    print("""Select a cipher: 
             1.  Caesar
             2.  ATBASH
             3.  Polybi_square
             4.  Exit
      """)
    select: int = int(input())
    if select == 4: 
        exit_flag = 1
        sys.exit()

    if select not in [1,2,3,4]: 
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
        Caesar(text_format, operation)
        print()

    if select == 2: 
        ATBASH(text)
        print()

    if select == 3: 
        Polybi_square(text_format, operation)
        print()