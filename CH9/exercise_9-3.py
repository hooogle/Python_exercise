class User():
    def __init__(self, first_name, last_name, **info):
        self.user_info = {}
        self.user_info['first_name'] = first_name
        self.user_info['last_name'] = last_name
        for key, value in info.items():
            self.user_info[key] = value
    def describe_user(self):
        print(self.user_info)
    def greet_user(self):
        print("Hello, " + self.user_info['first_name'] + ' ' + self.user_info['last_name'] + '.')
user1 = User('li','ou',city = 'beijing')
user1.describe_user()
user1.greet_user()

