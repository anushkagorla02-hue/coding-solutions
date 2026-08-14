# LPYAS110B

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Write a program that uses a while loop to find no. of vowels in given input string of lowercase latin letters.

 **Note:**  Vowels in lowercase latin letters are:  **a**,  **e**,  **i**,  **o**  and  **u**.

### Input Format
- The only line of input contains a string.
### Output Format
- The only line of output contains a single integer - The count of vowels in the input string.
### Sample 1:
Input
Output

```
codechef
```

```
3
```

### Explanation:

codechef has 3 vowels:  **o**,  **e**  and another  **e**

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-14T14:53:55.604Z  

```py
# cook your dish here
a=input()
l="aeiou"
count=0
i=0
while i<len(a):
    if a[i] in l:
        count+=1
    i+=1
print(count)

```

---

[View on CodeChef](https://www.codechef.com/problems/LPYAS110B)