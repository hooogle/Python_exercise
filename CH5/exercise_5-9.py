usrs = ['admin','adam','bob','jack','mary']
usrs = []
if usrs:
    for usr in usrs:
        if usr == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print('Hello ' + usr + ', thank you for logging in again.')
else:
    print('We need to find some users!')