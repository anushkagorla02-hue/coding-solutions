# JUMPCOST

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Jumping Cost

You have an array $A$ of $N$ elements.

You are currently at index $1$ with a balance of $0$, and you can do the following jump operation as many times as you want:

- Choose to jump from index $i$ to index $j$ ($i < j$), and add $(A_j - j + i)$ to your balance.

Find the maximum possible balance you can have at any point using these jump operations.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input. The first line contains a single integer $N$. The second line contains $N$ integers - $A_1, A_2, \ldots, A_N$.
### Output Format

For each test case, output on a new line the maximum balance you can have.

### Constraints
- $1 \le T \le 100$
- $2 \le N \le 100$
- $-100 \le A_i \le 100$
### Sample 1:
Input
Output

```
3
6
5 5 -1 5 -1 1
5
5 5 5 5 5
3
-4 -1 -5

```

```
7
16
0

```

### Explanation:

 **Test Case 1:**  Optimal is to jump from index $1$ to $2$ and then to $4$.

 **Test Case 3:**  Optimal is to not take any jumps at all.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-05T16:02:32.524Z  

```py
# cook your dish here
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    balance = 0
    ans = 0
    curr = 0

    while curr < n - 1:
        best = -1000000
        next_pos = -1

        for j in range(curr + 1, n):
            gain = a[j] - (j + 1) + (curr + 1)
            if gain > best:
                best = gain
                next_pos = j

        if best <= 0:
            break

        balance += best
        ans = max(ans, balance)
        curr = next_pos

    print(ans)
```

---

[View on CodeChef](https://www.codechef.com/problems/JUMPCOST)