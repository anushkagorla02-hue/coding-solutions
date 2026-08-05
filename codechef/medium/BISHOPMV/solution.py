# cook your dish here
t=int(input())
for _ in range(t):
    x1,y1,x2,y2= map(int,input().split())
    if x1==x2 and y1==y2:
        print(0)
    elif (x1+y1)%2 != (x2+y2)%2:
        print(-1)
    elif (x1-x2)==(y1-y2):
        print(1)
    else:
        print(2)