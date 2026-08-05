# cook your dish here
def solve():
    n,x,y=map(int,input().split())
    if n<=3:
        cost=n*x
    else:
        cost=(3*x)+((n-3)*y)
    print(cost)
cases=int(input())
for _ in range(cases):
    solve()