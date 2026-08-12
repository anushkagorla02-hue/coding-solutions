# PPSC94

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Sum of Even Integers

Listen

You are given an integer $N$.

You need to output the sum of all even integers from 1 to $N$.
Check the sample output given below.

### Sample 1:
Input
Output

```
5
```

```
6
```

### Sample 2:
Input
Output

```
10
```

```
30
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-12T17:17:46.703Z  

```py
# cook your dish here
N = int(input())
sum = 0

for i in range(1, N + 1):
    if i % 2 == 0:
        sum = sum + i

print(sum)
```

---

[View on CodeChef](https://www.codechef.com/problems/PPSC94)