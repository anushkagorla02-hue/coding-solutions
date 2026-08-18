# LPYASM17

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given a dictionary in the IDE containing a user's details.

You need to create 2 lists

- List 1 to contain all the keys
- List 2 to contain all the values

Output the list containing the keys on the 1st line.
Output the list containing values on the 2nd line.

### Expected output

```
['name', 'age', 'city', 'rating', 'nationality']
['John', 25, 'New York', 1550, 'Indian']

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-18T15:35:34.562Z  

```py
# Update your code below
person = {
    "name": "John",
    "age": 25,
    "city": "New York",
    "rating": 1550,
    "nationality": "Indian"
}
list1=list(person.keys())
list2=list(person.values())
print(list1)
print(list2)
```

---

[View on CodeChef](https://www.codechef.com/problems/LPYASM17)