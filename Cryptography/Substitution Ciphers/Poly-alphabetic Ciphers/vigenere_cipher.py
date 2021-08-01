def encrypt(plain_text, key):
    encrypted_text = ""

    for i in range(len(plain_text)):
        index = alpha.find(plain_text[i].upper()) + alpha.find(key[i])

        if plain_text[i].isupper():
            encrypted_text += alpha[index % 26]

        elif plain_text[i].islower():
            encrypted_text += alpha[index % 26].lower()

        else:
            encrypted_text += plain_text[i]

    return encrypted_text


def decrypt(cipher_text, key):
    decrypted_text = ""

    for i in range(len(cipher_text)):
        index = alpha.find(cipher_text[i].upper()) - alpha.find(key[i])

        if cipher_text[i].isupper():
            decrypted_text += alpha[index % 26]

        elif cipher_text[i].islower():
            decrypted_text += alpha[index % 26].lower()

        else:
            decrypted_text += cipher_text[i]

    return decrypted_text


def validKey(text, key):
    if len(text) == len(key):
        return key

    else:
        for i in range(len(text) - len(key)):
            key += key[i % len(key)]

        return key


if __name__ == "__main__":

    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    print("CHOICE -\n\t1. Text Encryption\n\t2. Text Decryption\n")

    choice = int(input("Enter your Choice : "))

    if choice == 1:
        P = input("\nEnter Text to Encrypt : ")
        k = input("Enter Key : ").upper()

        print('\nEncrypted Text is \033[1m"' + encrypt(P, validKey(P, k)) + '"\033[0m')

    elif choice == 2:
        C = input("\nEnter Text to Decrypt : ")
        k = input("Enter Key : ").upper()

        print('\nDecrypted Text is \033[1m"' + decrypt(C, validKey(C, k)) + '"\033[0m')

    else:
        print("Enter Valid Choice !!")
