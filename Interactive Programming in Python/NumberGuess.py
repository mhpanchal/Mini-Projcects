import simplegui as gui
import random

no_range = 100
left_guesses = 7
secret_no = 0


# helper function to start and restart the game

def new_game():
    # initialize global variables used in your code here
    global no_range
    global left_guesses
    global secret_no
    
    secret_no = random.randrange(0, no_range)
    
    if no_range == 100:
        left_guesses = 7
    elif no_range == 1000:
        left_guesses = 10
    
    print 'New Game...!!'
    print 'The range is from 0 to', no_range
    print 'You have', left_guesses, 'Guesses.'
    print 'Good Luck :)\n'


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global no_range
    no_range = 100
    new_game()

    
def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global no_range
    no_range = 1000
    new_game()
  
    
def input_guess(guess):
    # main game logic goes here	
    global left_guesses
    global secret_no
    
    g = int(guess)
    won = False
    left_guesses -= 1
    
    print 'You Guessed -', g
    print 'Number of Remaining Guesses -', left_guesses
    
    if g == secret_no:
        won = True
    elif g > secret_no:
        res = 'Lower!'
    else:
        res = 'Higher!'
        
    if won:
        print 'Hurray! You Guessed Correctly...'
        print 'You won the Game!!!\n'
        new_game()
    elif left_guesses == 0:
        print 'You did not Guess in given time. Game Over...'
        print 'The number was', secret_no
        print''
        new_game()
    else:
        print res
        print ''
    
    
    
# create frame
f = gui.create_frame("Game: Guess the number!", 250, 250)

# register event handlers for control elements and start frame
f.add_button("Range is [0, 100)", range100, 200)
f.add_button("Range is [0, 1000)", range1000, 200)	
f.add_input("Enter Your Guess", input_guess, 200)

# call new_game 
new_game()
f.start()
