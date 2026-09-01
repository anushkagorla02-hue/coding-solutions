import random

#complete this function to generate a random number between 1 and 100 
def getRandomNumber():
    return ran


def runGuess():
    secretNumber = getRandomNumber()
    print("The number is", secretNumber)


if __name__ == '__main__':
    ran=random.randrange(1,100)
    runGuess()