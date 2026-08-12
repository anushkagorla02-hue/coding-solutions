# cook your dish here
t=int(input())
for _ in range(t):
    n,m,x=map(int,input().split())
    r=(x+m-1)//m
    print(min(r,n-r+1))