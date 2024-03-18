import sys
from block_A_simple_replacement_ciphers import *
from block_B_multivalued_substitution_ciphers import *
from block_C_block_replacement_ciphers import *
from block_D_permutation_ciphers import *
from block_E_gamming_ciphers import *
from block_F_stream_ciphers import *
from block_G_combination_ciphers import *
from block_H_asynchronous_ciphers import *
from block_I_digital_signature_algorithms import *
from block_J_digital_signature_standards import *
from block_K_Diffie_Hellman_key_exchange import *


def main():
    while True:

        print("""Select an algorithm: 
                 1.   Caesar cipher
                 2.   ATBASH cipher
                 3.   Polybi_square
                 4.   Trithemius cipher
                 5.   Belazo cipher
                 6.   Vigenere cipher
                 7.   Playfair cipher
                 8.   Matrix cipher
                 9.   Cardano grid
                 10.  Vertical permutation
                 11.  Shannon's notebook
                 12.  A5/1
                 13.  МАГМА
                 14.  AES
                 15.  RSA
                 16.  ElGamal
                 17.  EСС
                 18.  DS RSA
                 19.  DS ElGamal
                 20.  DS GOST R 34.10-94
                 21.  DS GOST R 34.10-2012
                 22.  Diffie-Hellman key exchange
                 23.  Exit
             """)
        select: int = int(input())
        match select:
            case 22: Diffie_Hellman()
            case 23: sys.exit()

        if select not in [i for i in range(1, 23)]:
            print("Wrong select!")
            continue

        if select not in [18, 19, 20, 21]:
            print(""" Select an action: 
                        1. Encryption 
                        2. Decryption""")
        else:
            print(""" Select an action: 
                        1. Signing 
                        2. Сonfirmation
                      """)

        operation: int = int(input())
        if operation not in [1, 2]:
            print("Wrong select!")
            continue

        text = str(input('Enter text: '))
        print()

        if operation == 1:

            for i in range(len(text)):

                if text.find('.') != -1:
                    index = text.find('.')
                    text = text[:index] + 'тчк' + text[index + 1:]

                if text.find(',') != -1:
                    index = text.find(',')
                    text = text[:index] + 'зпт' + text[index + 1:]

                if text.find(' ') != -1:
                    index = text.find(' ')
                    text = text[:index] + 'прб' + text[index + 1:]

        elif select not in [8, 13, 14, 15, 16, 17, 18, 19]:
            text = text.replace(' ', '')

        match select:

            case 1: Caesar(operation, text.lower())
            case 2: ATBASH(operation, text.lower())
            case 3: Polybi_square(operation, text.lower())
            case 4: Trithemius_cipher(operation, text.lower())
            case 5: Belazo_cipher(operation, text.lower())
            case 6: Vigenere(operation, text.lower())
            case 7: Playfair_cipher(operation, text.lower())
            case 8: matrix_cipher(operation, text.lower())
            case 9: Cardano_grid(operation, text.lower())
            case 10: vertical_permutation(operation, text.lower())
            case 11: Shannon_notebook(operation, text.lower())
            case 12: A5_1(operation, text.lower())
            case 13: magma(operation, text.lower())
            case 14: aes(operation, text.lower())
            case 15: RSA(operation, text.lower())
            case 16: ElGamal(operation, text.lower())
            case 17: ECC(operation, text.lower())
            case 18: RSA_sign(operation, text.lower())
            case 19: ElGamal_sign(operation, text.lower())
            case 20: GOSTR_34_10_94(operation, text.lower())
            case 21: GOSTR_34_10_2012(operation, text.lower())


if __name__ == '__main__':
    main()

# A5/1 key: 0101001000011010110001110001100100101001000000110111111010110111
# MAGMA key: ffeeddccbbaa99887766554433221100f0f1f2f3f4f5f6f7f8f9fafbfcfdfeff
