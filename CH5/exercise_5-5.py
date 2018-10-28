def points(alien_color):
    if alien_color == 'green':
        print("You win 5 points!")
    elif alien_color == 'yellow':
        print("You win 10 points!")
    elif alien_color == 'red':
        print('You win 15 points!')
points('green')
points('yellow')
points('red')