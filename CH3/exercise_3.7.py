names = ['alice', 'bob', 'jack', 'milla']
for name in names:
    print(name.title() + ', would you like to have dinner with me?')
print("I got a bigger dinner table!!!")
names.insert(0,'james')
names.insert(2,'sakura')
names.append('tom')
for name in names:
    print(name.title() + ', would you like to have dinner with me?')
print("I'm sorry, the new dinner table won't be delieveried, I can only invite two perpons.")
while len(names) > 2:
    popped_person = names.pop()
    print(popped_person + ", I'am sorry you are now in the new list.")
for name in names:
     print(name.title() + ', would you like to have dinner with me?')
del names[:]
print(names)
