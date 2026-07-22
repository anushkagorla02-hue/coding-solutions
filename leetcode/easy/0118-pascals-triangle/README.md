# Pascal's Triangle

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an integer `numRows`, return the first numRows of  **Pascal's triangle**.

In  **Pascal's triangle**, each number is the sum of the two numbers directly above it as shown:

 

 **Example 1:** 

```
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

```

 **Example 2:** 

```
Input: numRows = 1
Output: [[1]]

```

 

 **Constraints:** 

- 1 <= numRows <= 30

## Solution

**Language:** Python  
**Runtime:** 2 ms (beats 17.46%)  
**Memory:** 12.2 MB (beats 94.37%)  
**Submitted:** 2026-07-22T16:37:41.167Z  

```py
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result=[]
        for i in range(numRows):
            row=[1]*(i+1)
            for j in range(1,i):
                row[j]=result[i-1][j-1]+result[i-1][j]
            result.append(row)
        return result
```

---

[View on LeetCode](https://leetcode.com/problems/pascals-triangle/)