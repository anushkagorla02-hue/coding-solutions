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