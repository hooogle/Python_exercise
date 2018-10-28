usrs = ['admin','adam','bob','jack','mary']
for usr in usrs:
    if usr == 'admin':
        print('Hello admin, would you like to see a status report?')
    else:
        print('Hello ' + usr + ', thank you for logging in again.')