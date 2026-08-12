# PPSC94

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Prime Number

Listen

The last challenge of the while loop.

Chef wants to write a code which checks if a given number is prime.

- You are given a whole number N.
- Your task is to determine if N is a prime number or not and print "Yes" if it is prime, or "No" if it is not.
### Sample 1:
Input
Output

```
14635
```

```
No
```

### Sample 2:
Input
Output

```
13
```

```
Yes
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-12T17:16:05.398Z  

```py
n = int(input())
isPrime = True # Assume n is prime

i = 2
while i < n:
    # Update your code below this line
    if n%i==0:
        isPrime=False
        break
    
    i+=1
if isPrime:
    print('Yes')
else:
    print('No')
```

---

[View on CodeChef](https://www.codechef.com/problems/PPSC94)