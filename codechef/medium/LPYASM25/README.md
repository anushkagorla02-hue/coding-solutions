# LPYASM25

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given two 24-hour format times as integers:
time1 = 1430 (2:30 PM)
time2 = 1615 (4:15 PM)

You need to calculate the difference between time2 and time1 in minutes using only operators.
Print the difference to the console.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-03T18:57:11.966Z  

```py
# cook your dish here
t1=1430
t2=1615
h1=t1//100
m1=t1%100
tot1=(h1*60)+m1
h2=t2//100
m2=t2%100
tot2=(h2*60)+m2
print(tot2-tot1)

```

---

[View on CodeChef](https://www.codechef.com/problems/LPYASM25)