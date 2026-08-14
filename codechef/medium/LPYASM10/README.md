# LPYASM10

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Create a function called password_validator that takes a password string as input from the user.

You need to output True if the password meets all requirements, False otherwise.
Requirements are as follows

- Password is at least 8 characters long
- Password contains at least one uppercase letter, and
- Password contains at least one number.

Check the sample input / output below for further clarity.

### Input Format

1st line of input contains 2 space separated integers.
2nd line of input contains one of the following characters - '+', '-', '*', '/'

### Sample 1:
Input
Output

```
abc123
```

```
False
```

### Sample 2:
Input
Output

```
abcdefgh
```

```
False
```

### Explanation:

Missing at least 1 uppercase character and 1 number

### Sample 3:
Input
Output

```
abcDef123
```

```
True
```

### Explanation:

Meets all 3 requirements

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-14T19:07:51.693Z  

```py
def password_validator(password):
    # complete the function 
    if len(password)<8:
        return False
    hasupper=False
    hasdigit=False
    for char in password:
        if char.isupper():
            hasupper=True
        if char.isdigit():
            hasdigit=True
    if hasupper and hasdigit:
        return True
    else:
        return False
    
    
    

password = input()
result = password_validator(password)
print(result)
```

---

[View on CodeChef](https://www.codechef.com/problems/LPYASM10)