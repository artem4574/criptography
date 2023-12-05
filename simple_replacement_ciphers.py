listalf = ["а", "б", "в", "г", "д", "е", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
hard_dictionary = {
    "а":"11", "б":"12", "в":"13", "г":"14", "д":"15", "е":"16",
    "ё":"21", "ж":"22", "з":"23", "и":"24", "й":"25", "к":"26",
    "л":"31", "м":"32", "н":"33", "о":"34", "п":"35", "р":"36",
    "с":"41", "т":"42", "у":"43", "ф":"44", "х":"45", "ц":"46",
    "ч":"51", "ш":"52", "щ":"53", "ъ":"54", "ы":"55", "ь":"56",
    "э":"61", "ю":"62", "я":"63"}

def Caesar():
    text: str = str(input('Enter text: '))
    shift: int = int(input('Enter shift: '))
    print(""" Select an action: 
            1. Encryption 
            2. Decryption""")
    operation: int = int(input())
    result_text, text, k = "", text.replace(' ', ''), 0
    if (operation == 1):
        for i in range(len(text)): result_text += (listalf[(listalf.index(text[i]) + shift) % 32])
    else:
        for i in range(len(text)): result_text += (listalf[(listalf.index(text[i]) - shift) % 32])
    print("Encrypted text: ", end=' ')
    for i in result_text:
        print(i, end='')
        k += 1
        if k % 5 == 0: print(" ", end='')
    print()

def ATBASH():
    text: str = str(input('Enter text: '))
    result_text, text, k = "", text.replace(' ', ''), 0
    for i in range(len(text)): result_text += (listalf[-listalf.index(text[i])-1])
    print("Encrypted/decrypted text: ", end=' ')
    for i in result_text:
        print(i, end='')
        k += 1
        if k % 5 == 0: print(" ", end='')
    print()

def Polybi_square():
    text: str = str(input('Enter text: '))
    print(""" Select an action: 
             1. Encryption 
             2. Decryption""")
    operation: int = int(input())
    result_text, text, k, step, list_fraze = "", text.replace(' ', ''), 0, 2,  []
    if (operation==1):
        for x in text: result_text += hard_dictionary.get(x)
        print("Encrypted text: ", end=' ')
        for i in result_text:
            print(i, end='')
            k += 1
            if k % 5 == 0: print(" ", end='')
        print()
    else:
        for i in range(0, len(text), 2):
            list_fraze.append(text[i:step])
            step += 2
        key_hard_dictionary_list = list(hard_dictionary.keys())
        val_hard_dictionary_list = list(hard_dictionary.values())
        for x in list_fraze: result_text += key_hard_dictionary_list[val_hard_dictionary_list.index(x)]
        print("Decrypted text: ", end=' ')
        for i in result_text:
            print(i, end='')
            k += 1
            if k % 5 == 0: print(" ", end='')
        print()

print(((24**9 * 62**8)%67)%11)



