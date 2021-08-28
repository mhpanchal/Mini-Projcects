def encrypt(plain_text, depth):
    encrypted_text = ""
    rfence = [[] for _ in range(depth)]
    d = 0
    flag = 1

    for i in plain_text:
        rfence[d].append(i)
        d += flag

        if d == 0 or d == depth - 1:
            flag = -flag

    for i in range(len(rfence)):
        encrypted_text += ''.join(rfence[i])

    return encrypted_text


def decrypt(cipher_text, depth):
    decrypted_text = ""
    rfence = [[] for _ in range(depth)]
    dummy = [[] for _ in range(depth)]
    length = len(cipher_text)
    d = 0
    flag = 1

    for i in cipher_text:
        dummy[d].append(i)
        d += flag

        if d == 0 or d == depth - 1:
            flag = -flag

    d = 0

    for i in dummy:
        for _ in range(len(i)):
            rfence[d].append(cipher_text[0])
            cipher_text = cipher_text[1::]

        d += 1

    d = 0
    flag = 1

    for _ in range(length):
        decrypted_text += rfence[d][0]
        rfence[d].remove(rfence[d][0])
        d += flag

        if d == 0 or d == depth - 1:
            flag = -flag

    return decrypted_text


if __name__ == "__main__":

    print("CHOICE -\n\t1. Text Encryption\n\t2. Text Decryption\n")

    choice = int(input("Enter your Choice : "))

    if choice == 1:
        P = input("\nEnter Text to Encrypt : ")
        d = int(input("Enter Depth : "))

        print('\nEncrypted Text is \033[1m"' + encrypt(P, d) + '"\033[0m')

    elif choice == 2:
        C = input("\nEnter Text to Decrypt : ")
        d = int(input("Enter Depth : "))

        print('\nDecrypted Text is \033[1m"' + decrypt(C, d) + '"\033[0m')

    else:
        print("Enter Valid Choice !!")
