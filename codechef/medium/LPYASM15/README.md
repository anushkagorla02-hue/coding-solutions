# LPYASM15

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given a dictionary in the IDE - student names and their respective scores on a math test.

You need to write the code to perform the following

- Accept user input - the student name and their updated score
- Update the dictionary for the specific student with their new score
- Print the dictionary to the console.

Check the output below for further clarity.

### Sample 1:
Input
Output

```
Bob
95
```

```
{'Alice': 85, 'Bob': 95, 'Charlie': 78}
```

### Sample 2:
Input
Output

```
Alice
80
```

```
{'Alice': 80, 'Bob': 92, 'Charlie': 78}
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-18T15:42:10.215Z  

```py
# Update your code below
scores = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}
name=input()
marks=int(input())
scores[name]=marks
print(scores)
```

---

[View on CodeChef](https://www.codechef.com/problems/LPYASM15)