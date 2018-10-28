names = ['alice', 'bob', 'jack', 'milla']
for name in names:
    print(name.title() + ', would you like to have dinner with me?')
print("I got a bigger dinner table!!!")
names.insert(0,'james')
names.insert(2,'sakura')
names.append('tom')
for name in names:
    print(name.title() + ', would you like to have dinner with me?')
