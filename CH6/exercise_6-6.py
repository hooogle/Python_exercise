favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
friends = ['phil', 'sarah','tom','milla']
for name in friends:
    if name in favorite_languages.keys():
        print('Thank you for taking the poll.')
    else:
        print(name + ', please thake our poll')