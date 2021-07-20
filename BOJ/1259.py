while True:
    string = input()
    if string == '0':
        exit()
    reverse_string = string[::-1]
    if string == reverse_string:
        print('yes')
    else:
        print('no')