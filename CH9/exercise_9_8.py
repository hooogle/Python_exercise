class User():
    def __init__(self, first_name, last_name, **info):
        self.login_attempts = 0
        self.user_info = {}
        self.user_info['first_name'] = first_name
        self.user_info['last_name'] = last_name
        for key, value in info.items():
            self.user_info[key] = value
    def describe_user(self):
        print(self.user_info)
    def greet_user(self):
        print("Hello, " + self.user_info['first_name'] + ' ' + self.user_info['last_name'] + '.')
    def increment_login_attempts(self):
        self.login_attempts = self.login_attempts + 1
    def reset_login_attempts(self):
        self.login_attempts = 0


class Proviledges():
    def __init__(self, *privileges):
        self.privileges = privileges
    def show_privileges(self):
        print(self.privileges)


class Admin(User):
    def __init__(self, first_name, last_name, **info):
        super().__init__(first_name, last_name, **info)
        self.privileges = Proviledges('can add post', 'can delete post', 'can ban user')
    

admin1 = Admin('zhang', 'san')
admin1.privileges.show_privileges()