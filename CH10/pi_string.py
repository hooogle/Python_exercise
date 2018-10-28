filename = 'CH10/pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string[:52] + '...')
print(len(pi_string))

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi.")
else:
    print("Your birthday does not appear in the first million digits of pi.")

not_appear_num = 0
not_appear = []
for number in range(100000,1000000):
    if str(number) not in pi_string:
        print("New number not found" + str(not_appear_num))
        not_appear_num += 1
        not_appear.append(number)
print(not_appear_num)
print(not_appear[:50])
