# cook your dish here
a,b=map(int,input().split())
s="No"
for i in range(a+1,b):
    if a!=b or i%2==0:
        s="Yes"
        break
print(s)