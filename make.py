def main():
    print('[1]: Create All 3 chars from a-z')
    print('[2]: Create All 3 chars from a-z with symbols')
    print('[3]: Create All 3 chars from a-z with numbers')
    print('[4]: Create All 3 chars from a-z with numbers & symbols')
    option = int(input('Option: '))

    if option == 1:
        write_chars('abcdefghijklmnaopqrstuvwxyz')
    elif option == 2:
        write_chars('abcdefghijklmnaopqrstuvwxyz-_')
    elif option == 3:
        write_chars('abcdefghijklmnaopqrstuvwxyz1234567890')
    elif option == 4:
        write_chars('abcdefghijklmnaopqrstuvwxyz121234567890-_')

def write_chars(chars):
    file = open("output.txt", "w")

    for firstchar in chars:
        for secondchar in chars:
            for thridchar in chars:
                file.write(f"{firstchar}{secondchar}{thridchar}\n")
    
    print('Wrote all to file please check your folder!')


if __name__ == "__main__":
    main()
