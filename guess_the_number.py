
import random, sys, time, os, subprocess

def startup():
    print('Welcome to guess the number:) Please type the max amount of numbers to guess from')
#run startup
startup()
#the users input will be the max range of the random numbers
setmax = int(input())
secret_number = random.randint(0, setmax)
print('guess a number between 0-' + str(setmax))

def winner():
    print('Congratulations:), you got it! The number was ' + str(secret_number))
    time.sleep(2)
    print('Type retry to play again, or anything else to quit')
    if input() == 'retry':
        #to restart program use following line
        subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:])
    else:
        sys.exit()
# Used a while loop or use: for guesstries in range(6):
def guess_number():
    guessedtries = 0
    tries_left = 6 
    while guessedtries <= 7:
        print('what is your guess?')
        guess_number = int(input())
        guessedtries = guessedtries + 1
        if guess_number == secret_number:
            guessedtries = 0
            winner()
        elif guess_number < secret_number:
            tries_left = tries_left - 1
            print('You are too low, try again you have ' + str(tries_left) + ' tries left')
        elif guess_number > secret_number:
            tries_left = tries_left - 1
            print('You are too high, try again you have ' + str(tries_left) + ' tries left')
        if guessedtries == 6:
            print('Nice try, the number was ' + str(secret_number) + '. Type retry to play again, or anything else to quit')
            if input() == 'retry':
                subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:])
            else:
                sys.exit()

guess_number()

if __name__ == '__main__':
    # Script2.py executed as script
    # do something
    startup()
    