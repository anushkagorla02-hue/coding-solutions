# PPSC96

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Fibonacci Series

Listen

You are given an integer $N$.

You need to output the first $N$ numbers of the Fibonacci Series.
Check the sample output given below.

 **Note:**  A Fibonacci number is a series of numbers in which each number is obtained by adding the two preceding numbers.

F1 = 0, F2 = 1
FN = FN-2 + FN-1

### Sample 1:
Input
Output

```
5
```

```
0 1 1 2 3
```

### Sample 2:
Input
Output

```
8
```

```
0 1 1 2 3 5 8 13
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-12T17:25:23.555Z  

```py
# Update the '_' to solve the problem

n = int(input())
a = 0
b = 1

print(a, b, end=" ")


for i in range(n-2):
    c = a+b # set currrent number as sum of previous two numbers
    print(c, end=" ")
    # Update a and b as next two numbers
    a = b
    b=c
```

---

[View on CodeChef](https://www.codechef.com/problems/PPSC96)