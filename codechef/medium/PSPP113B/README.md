# PSPP113B

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Length and count of elements in a tuple

Listen

For tuples, `len()` returns the number of elements.

```
my_tuple = (1, 2, 3, 4, 5)
print("Length of the tuple:", len(my_tuple))  # Output: Length of the tuple: 5

```

For tuples, `count()` allows you to count the occurrences of a specified value.

```
my_tuple = (1, 2, 2, 3, 2, 4, 5, 2)
print("Number of occurrences of 2:", my_tuple.count(2))  # Output: Number of occurrences of 2: 4

```

### Task

What is the expected output for the following code?

```
student = ([2, 2], [2, 2, 2], 2, 3)
print(len(student))
print(student.count(2))

```

## Solution

**Language:** C++  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-18T15:27:18.909Z  

```cpp
student = (["Alice", "Bob"], ["Math", "Science", "English"], 20, 'XYZ')

# Update the code below this line
list1,list2,num,string=student
print(list1[1])
print(list2[2])
print(num)
print(string[2])
```

---

[View on CodeChef](https://www.codechef.com/problems/PSPP113B)