current_users = ['admin','adam','bob','jack','mary']
new_users = ['alice','Bob','MILLA','JACK','tom']
for new_user in new_users:
    if new_user.lower() in current_users:
        print('Please enter another user name:')
    else:
        print('This user name is OK')