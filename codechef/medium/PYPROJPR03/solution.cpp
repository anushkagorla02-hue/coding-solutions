    user_guess = int(input("Enter a number between 1 and 100: "))
def runGuess():
    secretNumber = getRandomNumber()
        return "Hot"


    elif guess==number:
        return "Right"
    else:
    if guess>(number+10) or guess<(number-10):
        return "Cold"

#Update the code below to solve the problem
def giveHint(number, guess):
def getRandomNumber():
    return random.randrange(1, 100)
    hint = giveHint(secretNumber, user_guess)
    if hint == "Right":
        print("You guessed it Right!")
    else:
        print(hint)
            
if __name__ == '__main__':
    runGuess()