# PPSC85

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Sum of N Integers

Listen

Chef was given an integer input N.

He wants to write a code using `while` loops to output the sum of all integers from 1 to $N$.
Help him complete the code by filling in the blanks.

### Sample 1:
Input
Output

```
5
```

```
15
```

### Sample 2:
Input
Output

```
10
```

```
55
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-12T17:10:08.027Z  

```py
# cook your dish here
n=int(input())
a=1
sum1=0
while a<n+1:
    sum1+=a
    a+=1
print(sum1)
```

---

[View on CodeChef](https://www.codechef.com/problems/PPSC85)