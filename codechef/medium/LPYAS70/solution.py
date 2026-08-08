# cook your dish here
a,b,c=map(int,input().split())
if a>b and a>c:
    if b>c:
        print("Increasing")
    else:
        print("Neither")
elif a<b and b<c:
    print("Decreasing")
else:
    print("Neither")