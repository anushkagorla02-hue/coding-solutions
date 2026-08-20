# Sum of Digits of a Five Digit Number

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

**Objective** 

The modulo operator, `%`, returns the remainder of a division.  For example, `4 % 3 = 1` and `12 % 10 = 2`.  The ordinary division operator, `/`, returns a truncated integer value when performed on integers.  For example, `5 / 3 = 1`.  To get the last digit of a number in base 10, use $10$ as the modulo divisor.  

**Task**

Given a five digit integer, print the sum of its digits.  


**Input Format**

The input contains a single five digit number, $n$.

**Constraints**

$ 10000 \le n \le 99999$  

**Output Format**

Print the sum of the digits of the five digit number.

## Solution

**Language:** C  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-20T16:45:37.802Z  

```c
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
	
    int n,t,sum;
    scanf("%d", &n);
    //Complete the code to calculate the sum of the five digits on n.
    
    while(n>0)
    {
       t=n%10;
       sum=sum+t;
       n=n/10;
    }
    printf("%d",sum);
    return 0;
}

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/sum-of-digits-of-a-five-digit-number/problem)