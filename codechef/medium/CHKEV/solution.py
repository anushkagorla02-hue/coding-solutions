# cook your dish here
a,b=map(int,input().split())
s="False"
for i in range(a+1,b):
    if a!=b or i%2==0:
        s="True"
        break
print(s)