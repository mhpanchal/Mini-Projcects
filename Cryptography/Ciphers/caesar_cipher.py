def encrypt(plain_text, shift):
    encrypted_text = ""

    for i in plain_text:

        if i.isupper():
            encrypted_text += chr((ord(i) + shift - ord('A')) % 26 + ord('A'))

        elif i.islower():
            encrypted_text += chr((ord(i) + shift - ord('a')) % 26 + ord('a'))

        else:
            encrypted_text += i

    return encrypted_text


def decrypt(cipher_text, shift):
    decrypted_text = ""

    for i in cipher_text:

        if i.isupper():
            decrypted_text += chr((ord(i) - shift - ord('A')) % 26 + ord('A'))

        elif i.islower():
            decrypted_text += chr((ord(i) - shift - ord('a')) % 26 + ord('a'))

        else:
            decrypted_text += i

    return decrypted_text


if __name__ == "__main__":

    print("CHOICE -\n\t1. Text Encryption\n\t2. Text Decryption\n")

    choice = int(input("Enter your Choice : "))

    if choice == 1:
        P = input("\nEnter Text to Encrypt : ")
        s = int(input("Enter no. of Shifts : "))
        print('\nEncrypted Text is \033[1m"' + encrypt(P, s) + '"\033[0m')

    elif choice == 2:
        c = input("\nDo you know the no. of Shifts? (Yes/No) ")

        if c.upper() == "Y" or c.upper() == "YES":
            C = input("\nEnter Text to Decrypt : ")
            s = int(input("Enter no. of Shifts : "))

            print('\nDecrypted Text is \033[1m"' + decrypt(C, s) + '"\033[0m')

        else:
            C = input("\nEnter Text to Decrypt : ")
            print("\nPossible Keys -")

            for n in range(1, 26):
                print('\t', n, ' Decrypted Text is \033[1m"' + decrypt(C, n) + '"\033[0m')


    else:
        print("Enter Valid Choice !!")
