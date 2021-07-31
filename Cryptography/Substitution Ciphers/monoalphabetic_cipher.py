def encrypt(plain_text, key):
    encrypted_text = ""

    for i in plain_text:

        if i.isupper():
            encrypted_text += key[alpha.find(i)]

        elif i.islower():
            encrypted_text += key[alpha.find(i.upper())].lower()

        else:
            encrypted_text += i

    return encrypted_text


def decrypt(cipher_text, key):
    decrypted_text = ""

    for i in cipher_text:

        if i.isupper():
            decrypted_text += alpha[key.find(i)]

        elif i.islower():
            decrypted_text += alpha[key.find(i.upper())].lower()

        else:
            decrypted_text += i

    return decrypted_text


def validKey(key):
    return set(key) == set(alpha)


if __name__ == "__main__":

    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    print("CHOICE -\n\t1. Text Encryption\n\t2. Text Decryption\n")

    choice = int(input("Enter your Choice : "))

    if choice == 1:
        P = input("\nEnter Text to Encrypt : ")
        k = input("Enter 26 Letters Long Key : ").upper()

        if validKey(k) is True:
            print('\nEncrypted Text is \033[1m"' + encrypt(P, k) + '"\033[0m')
        else:
            print("\nEnter Valid Key !!")

    elif choice == 2:
        C = input("\nEnter Text to Decrypt : ")
        k = input("Enter 26 Letters Long Key : ").upper()

        if validKey(k) is True:
            print('\nDecrypted Text is \033[1m"' + decrypt(C, k) + '"\033[0m')
        else:
            print("\nEnter Valid Key !!")

    else:
        print("Enter Valid Choice !!")
