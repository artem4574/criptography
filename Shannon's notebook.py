listalf = ["а", "б", "в", "г", "д", "е", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]


def digitization(open_text, result = []):
    for i in range(len(open_text)): result.append(listalf.index(open_text[i])+1)
    return result

print(digitization('один'))
def undigitization(ciphertext, result = []):
    for i in range(len(ciphertext)): result.append(listalf[ciphertext[i]-1])
    return result


def encrypt_text(text, gamma, encrypted_text = []):
    for i in range(len(text)): encrypted_text.append((text[i] + gamma[i]) % 32)
    return encrypted_text


def decrypt_text(text, gamma):
    dec_text = [0]*len(text)
    for i in range(len(text)):
        if gamma[i] < text[i]: dec_text[i] = text[i] - gamma[i]
        else: dec_text[i] = text[i] + 32 - gamma[i]
    return dec_text


def generate_gamma(a, c, t0, length):
    t, gamma = t0, []
    for i in range(length):
        t = (a * t + c) % 32
        gamma.append((a * t + c) % 32)
    return gamma


def main():
    a, c, t0, k = int(input("Enter the value of a (a % 4 = 1): ")), int(input("Enter the value of c (с % 2 != 0): ")) % 32, int(input("Enter the value of T0: ")), 0
    print(""" Select an action: 
        1. Encryption 
        2. Decryption""")
    choose: int = int(input())
    if choose == 1:
        open_text = str(input("Enter open text: "))
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