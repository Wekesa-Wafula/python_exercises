while True:
    password = str(input('Enter password:'))
    if password == 'q':
        break

    if len(password) < 5:
        print('too short')
    elif len(password) > 15:
        print('too many characters')
    else:
        print('login successful')
