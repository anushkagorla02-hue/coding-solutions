# cook your dish here
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    dp = [0] * n
    ans = 0

    for j in range(1, n):
        dp[j] = -10**10

        for i in range(j):
            gain = dp[i] + a[j] - (j + 1) + (i + 1)
            if gain > dp[j]:
                dp[j] = gain

        if dp[j] > ans:
            ans = dp[j]

    print(ans)