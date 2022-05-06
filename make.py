def main():
    number = int(input('Would you like to create a 2 char list or 3?: '))


    print(f'[1]: Create All {number} chars from a-z')
    print(f'[2]: Create All {number} chars from a-z with symbols')
    print(f'[3]: Create All {number} chars from a-z with numbers')
    print(f'[4]: Create All {number} chars from a-z with numbers & symbols')
    option = int(input('Option: '))


    if number == 3:
        if option == 1:
            write_chars('abcdefghijklmnaopqrstuvwxyz')
        elif option == 2:
            write_chars('abcdefghijklmnaopqrstuvwxyz-_')
        elif option == 3:
            write_chars('abcdefghijklmnaopqrstuvwxyz1234567890')
        elif option == 4:
            write_chars('abcdefghijklmnaopqrstuvwxyz121234567890-_')
    elif number == 2:
        if option == 1:
            write_chars_2('abcdefghijklmnaopqrstuvwxyz')
        elif option == 2:
            write_chars_2('abcdefghijklmnaopqrstuvwxyz-_')
        elif option == 3:
            write_chars_2('abcdefghijklmnaopqrstuvwxyz1234567890')
        elif option == 4:
            write_chars_2('abcdefghijklmnaopqrstuvwxyz121234567890-_')

def write_chars_2(chars):
    file = open("output.txt", "w")

    for firstchar in chars:
        for secondchar in chars:
                file.write(f"{firstchar}{secondchar}\n")
    
    print('Wrote all to file please check your folder!')

def write_chars(chars):
    file = open("output.txt", "w")

    for firstchar in chars:
        for secondchar in chars:
            for thridchar in chars:
                file.write(f"{firstchar}{secondchar}{thridchar}\n")
    
    print('Wrote all to file please check your folder!')


if __name__ == "__main__":
    main()
