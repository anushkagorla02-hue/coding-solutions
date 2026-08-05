# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    for i in range(1,n):
        for j in range(i):
            pos=a[i]-i+j
            if a[pos]:
                print(pos)