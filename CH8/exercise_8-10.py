def show_magicians(magicians):
    for magician in magicians:
        print(magician)
def make_great(magicians):
    for index in list(range(len(magicians))):
        magicians[index] = 'the Great ' + magicians[index]
magicians = ['aaa', 'bbb', 'sss']
show_magicians(magicians)
make_great(magicians)
show_magicians(magicians)