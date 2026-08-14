# LPYASM10

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Create a function called calculator that takes three parameters: two numbers and an operator (as a string: '+', '-', '*', '/').
The function should return the result of the operation.
If division by zero is attempted, return "Cannot divide by zero".
Check the sample input / output below for further clarity

### Input Format

1st line of input contains 2 space separated integers.
2nd line of input contains one of the following characters - '+', '-', '*', '/'

### Sample 1:
Input
Output

```
2 3
+
```

```
5
```

### Sample 2:
Input
Output

```
3 2
/
```

```
1.5
```

### Sample 3:
Input
Output

```
3 0
/

```

```
Cannot divide by zero
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-14T19:02:25.930Z  

```py
# Update the function below
def calculator(num1, num2, operator):
    if operator=='+':
        print(num1+num2)
    elif operator=='-':
        print(num1-num2)
    elif operator=='*':
        print(num1*num2)
    elif operator=='/':
        if num2==0:
            print("Cannot divide by zero")
        else:
            print(num1/num2)
    
num1, num2 = map(int, input().split())
operator = input()
calculator(num1, num2, operator)
```

---

[View on CodeChef](https://www.codechef.com/problems/LPYASM10)