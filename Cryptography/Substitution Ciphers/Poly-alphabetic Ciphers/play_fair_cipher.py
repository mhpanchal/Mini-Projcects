def encrypt(plain_text, key):
    encrypted_text = ""
    i = 0

    for s in range(0, len(plain_text) + 1, 2):
        if s < len(plain_text) - 1:
            if plain_text[s] == plain_text[s + 1]:
                plain_text = plain_text[:s + 1] + 'X' + plain_text[s + 1:]

    if len(plain_text) % 2 != 0:
        plain_text = plain_text[:] + 'X'

    while i < len(plain_text):
        curLoc = char_loc(plain_text[i])
        nextLoc = char_loc(plain_text[i + 1])

        if curLoc[0] == nextLoc[0]:
            encrypted_text += key[curLoc[0]][(curLoc[1] + 1) % 5]
            encrypted_text += key[nextLoc[0]][(nextLoc[1] + 1) % 5]
            encrypted_text += ' '

        elif curLoc[1] == nextLoc[1]:
            encrypted_text += key[(curLoc[0] + 1) % 5][curLoc[1]]
            encrypted_text += key[(nextLoc[0] + 1) % 5][nextLoc[1]]
            encrypted_text += ' '

        else:
            encrypted_text += key[curLoc[0]][nextLoc[1]]
            encrypted_text += key[nextLoc[0]][curLoc[1]]
            encrypted_text += ' '

        i += 2

    return encrypted_text.rstrip()


def decrypt(cipher_text, key):
    decrypted_text = ""
    i = 0

    while i < len(cipher_text):
        curLoc = char_loc(cipher_text[i])
        nextLoc = char_loc(cipher_text[i + 1])

        if curLoc[0] == nextLoc[0]:
            decrypted_text += key[curLoc[0]][(curLoc[1] - 1) % 5]
            decrypted_text += key[nextLoc[0]][(nextLoc[1] - 1) % 5]

        elif curLoc[1] == nextLoc[1]:
            decrypted_text += key[(curLoc[0] - 1) % 5][curLoc[1]]
            decrypted_text += key[(nextLoc[0] - 1) % 5][nextLoc[1]]

        else:
            decrypted_text += key[curLoc[0]][nextLoc[1]]
            decrypted_text += key[nextLoc[0]][curLoc[1]]

        i += 2

    return decrypted_text.rstrip('X')


def char_loc(ch):
    loc = []
    if ch =='J':
        ch ='I'

    for i, j in enumerate(k):
        for m, n in enumerate(j):
            if ch == n:
                loc.append(i)
                loc.append(m)

    return loc


def key_matrix(key):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    table = []

    for c in key:
        if c == 'J':
            c = 'I'

        if c not in table and c in alpha:
            table.append(c)

    for c in alpha:
        if c == 'J':
            c = 'I'

        if c not in table:
            table.append(c)

    matrix = [[0 for _ in range(5)] for _ in range(5)]
    index = 0

    for i in range(5):
        for j in range(5):
            matrix[i][j] = table[index]
            index += 1

    return matrix


if __name__ == "__main__":

    print("CHOICE -\n\t1. Text Encryption\n\t2. Text Decryption\n")

    choice = int(input("Enter your Choice : "))

    if choice == 1:
        P = input("\nEnter Text to Encrypt : ").replace(" ", "").upper()
        k = input("Enter Key : ").replace(" ", "").upper()

        k = key_matrix(k)

        print('\nEncrypted Text is \033[1m"' + encrypt(P, k) + '"\033[0m')

    elif choice == 2:
        C = input("\nEnter Text to Decrypt : ").replace(" ", "").upper()
        k = input("Enter Key : ").replace(" ", "").upper()

        k = key_matrix(k)

        print('\nDecrypted Text is \033[1m"' + decrypt(C, k) + '"\033[0m')

    else:
        print("Enter Valid Choice !!")
