import json

def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username = input("What is your name: ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def certificate_user(username):
    certificate = input("Do you " + username + "?(y/n): ")
    if certificate.lower == 'y':
        return True
    else:
        return False

def greet_user():
    username = get_stored_username()
    if username and certificate_user(username):
        print("Welcome back, " + username + "!")
    elif get_stored_username() == False:
        username = get_new_username()
    else:
        print("We'll remember you when you come back, " + username + "!")

greet_user()