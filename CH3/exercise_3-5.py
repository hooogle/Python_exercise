names = ['alice', 'bob', 'jack', 'mary']
for name in names:
    print(name.title() + ', would you like to have dinner with me?')
print("Mary won't come.")
names[3] = 'milla'
for name in names:
    print(name.title() + ', would you like to have dinner with me?')
