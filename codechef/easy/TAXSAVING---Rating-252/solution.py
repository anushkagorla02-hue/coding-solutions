# cook your dish here
test1=int(input())
for _ in range(test1):
    x,y=map(int,input().split())
    if x>y:
        print(x-y)