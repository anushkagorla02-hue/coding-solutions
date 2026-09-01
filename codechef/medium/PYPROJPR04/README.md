# PYPROJPR04

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Adding loop

Did you notice in the previous problem that we got only 1 guess.

Ideally - the system should prompt the user for another guess.

Can you think of a way to incorporate this using loops?

### Task

Add a `while` loop and a `break` statement to the `runGuess()` function to complete the project.
The ideal flow is the 'Secret number' and user guessed number are compared with the following result

- If the user guess is greater than or less than 'Secret number' by 10 - the system output is 'Cold' and the user is prompted to guess again
- If the user guess is + / - 10 from the 'Secret number' - the system output is 'Hot' and the user is prompted to guess again
- If the user guess matches the 'Secret number' - the system prompts 'You guessed it right!!' and the Project terminates

## Solution

**Language:** C++  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-01T15:22:42.616Z  

```cpp
        hint = giveHint(secretNumber, user_guess)
        if hint == "Right":
            print("You guessed it Right!")
            break
        else:
            print(hint)
            
if __name__ == '__main__':
    # Update the code below
    while True:
        user_guess = int(input("Enter a number between 1 and 100: "))
def runGuess():
    secretNumber = getRandomNumber()
    else:
        return "Hot"

        return "Cold"
    elif number == guess:
        return "Right"
    runGuess()
```

---

[View on CodeChef](https://www.codechef.com/problems/PYPROJPR04)