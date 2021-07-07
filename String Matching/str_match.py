def search(str_to_find, main_txt):
    pattern_found = 0

    for i in range(len(main_txt) - len(str_to_find) + 1):
        if txt[i:i + len(str_to_find)] == str_to_find:
            print("\nPattern Found at Index", i)
            print("\t" + txt[:i] + "\033[93m" + "\033[1m" + txt[i:i + len(str_to_find)] + "\033[0m" + txt[i + len(str_to_find):])
            pattern_found += 1

    else:
        if pattern_found == 0:
            print("\nPattern not Found")


if __name__ == '__main__':

    txt = input("Enter the main text : ")
    str_2_find = input("Enter the string you want to find : ")

    print('\nYou want to find "{str}" from "{text}" !'.format(str=str_2_find, text=txt))

    search(str_2_find, txt)
