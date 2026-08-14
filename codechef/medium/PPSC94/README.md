# PPSC94

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

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
**Submitted:** 2026-08-14T14:49:07.439Z  

```py
# cook your dish here
n=int(input())
sum=0
i=1
while i<=n:
    if i%2==0:
        sum+=i
    i+=1
print(sum)
```

---

[View on CodeChef](https://www.codechef.com/problems/PPSC94)