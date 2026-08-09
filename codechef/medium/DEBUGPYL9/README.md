# DEBUGPYL9

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Incorrect Index

Listen

Strings in Python have zero-based indexing.
This means that the first index is 0.
It is easy to forget that and use one-based indexing instead.
This incorrect indexing leads to another logical error.

 **Program to print the last character of the string** 

```
s = input()       # input string
n = len(s)        # find length of string

print(s[n - 1])   # Correct way to access the n-th character
print(s[n]) # incorrect way

```

### Task
- Given a program to print 1st, 4th and 6th character of a string
- Find out the logical error and solve it
### Sample 1:
Input
Output

```
hellohowudoing
```

```
hlh
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-09T18:25:54.617Z  

```py
# Change the indexing from one based to zero based
s = input() 

print(s[0] + s[3] + s[5])

```

---

[View on CodeChef](https://www.codechef.com/problems/DEBUGPYL9)