# cook your dish here
a,b=map(int,input().split())
s="False"
for i in range(a,b):
    if i%2==0:
        s="True"
print(s)