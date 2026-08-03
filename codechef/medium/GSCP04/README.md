# GSCP04

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### How to print output

Cool - so you learnt how to accept integer inputs.

Now let's look at how to convert input into output and display the same.

Most algorithmic programming problems will need you to generate the following types of output

- Integers or Floats
- Strings
- An array of integers or strings

Go ahead and try in the IDE.
Click on  **Submit**  to proceed.

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-03T18:18:25.265Z  

```c_cpp
//Click submit to continue
#include <stdio.h>

int main() {
    int N = 5;
    printf("%d\n", N);

    char s[10] = "abcde";
    printf("%s\n", s);

    int Arr[] = {2, 3, 6, 7};
    for (int i = 0; i < 4; i++) {
        printf("%d ", Arr[i]);
    }
    return 0;
}

```

---

[View on CodeChef](https://www.codechef.com/problems/GSCP04)