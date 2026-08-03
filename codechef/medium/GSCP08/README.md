# GSCP08

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### How to accept string inputs

Lets try the same exercise with strings.

### Task

You need to write a program that does the following

- Accepts $2$ space separated alphanumeric strings as input in $1^{st}$ line as the variables $A$, $B$
- Accepts $3$ space separated alphanumeric strings as input in $2^{nd}$ line as the variables $C$, $D$, $E$
- Accepts $4$ space separated alphanumeric strings as input in $3^{rd}$ line as the variables $F$, $G$, $H$, $I$
- Prints out $9$ space separated strings as output in a single line to the console

Remember that the $scanf()$ function necessarily takes the parameters to be strings.
Solve the problem in the IDE and then click on  **Submit**  to proceed.

 **Note-**  C treats all whitespace similarly while taking input.
So: scanf(“%d%d”, &a, &b);
And: scanf(“%d”, &a);
scanf(“%d”, &b);
are equivalent.

### Sample 1:
Input
Output

```
abc cde
fg hi jk
l m n o
```

```
abc cde fg hi jk l m n o
```

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-03T18:17:38.984Z  

```c_cpp
//fill the _ in the IDE to continue
#include <stdio.h>

int main() {
    char A[10], B[10];
    char C[10], D[10], E[10];
    char F[10], G[10],H[10],I[10];
    scanf("%s%s", A , B );
    scanf("%s%s%s", C, D, E );
    scanf("%s%s%s%s", F , G, H, I );
    printf("%s %s %s %s %s %s %s %s %s ", A , B , C , D , E , F , G , H , I );  
    return 0;
}

```

---

[View on CodeChef](https://www.codechef.com/problems/GSCP08)