step_1 = []
step_2 = []
step_3 = []
step_4 = []
def Cardano_grid():
    text: str = str(input('Enter text: '))
    print(""" Select an action: 
                    1. Encryption 
                    2. Decryption""")
    operation: int = int(input())
    result_text, text, k = [[0]*10 for i in range(6)], text.replace(' ', ''), 0
    if operation == 1:              # encryption

        print("Encrypted text: ", end=' ')
        for i in result_text:
            print(i, end='')
            k += 1
            if k % 5 == 0: print(" ", end='')
        print()
        exit()
    if operation == 2:               # decryption

        print("Decrypted text: ", end=' ')
        for i in result_text: print(i, end='')
        print()
        exit()
    else:
        print("Error in select!")
        exit()

# размер сетки
size = 10
# сетка
my_list = (
    ("тСПвнперот"),
    ("ьеосФдптор"),
    ("оеевнйисст"),
    ("оттаряяевл"),
    ("лбюящ-оялд"),
    ("еуитсоочюб"),
    ("нионсызймх"),
    ("шмеянситор"),
    ("уфкртгтооо"),
    ("кудррвуоа."))

# решетка Кардано
grid = (
    (0, 1, 0, 0, 0, 0, 1, 0, 0, 1),
    (1, 0, 0, 0, 1, 0, 0, 0, 0, 0),
    (0, 1, 0, 0, 0, 1, 0, 0, 1, 0),
    (0, 0, 1, 0, 0, 0, 0, 1, 0, 0),
    (1, 0, 0, 1, 0, 1, 1, 0, 0, 1),
    (0, 0, 1, 0, 0, 0, 0, 0, 0, 0),
    (1, 1, 0, 0, 0, 0, 1, 0, 1, 0),
    (0, 0, 1, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 1, 0, 0, 0, 1, 0),
    (0, 0, 1, 0, 0, 0, 0, 1, 0, 0))

for i in range(size):
    for j in range(size):
        if grid[i][j] == 1:
            result_text += my_list[i][j]

for i in range(size):
    for j in range(size):
        if grid[size - j - 1][i] == 1:
            result_text += my_list[i][j]

for i in range(size):
    for j in range(size):
        if grid[size - i - 1][size - j - 1] == 1:
            result_text += my_list[i][j]

for i in range(size):
    for j in range(size):
        if grid[j][size - i - 1] == 1:
            result_text += my_list[i][j]

'''
    два кейса: 6x10 и 10x10
    вариативность зависиит от размера входного текста
    запись одну строку и дробление на массив
    шифровка и дешифровка происходит по одному принципу - чтение в 4 массива
'''