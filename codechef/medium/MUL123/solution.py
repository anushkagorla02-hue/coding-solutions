# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    if n%3==0:
        print(0)
    elif n%3==2 or ((n//5+1)*5)%3==0:
        print(1)
    else:
        print(2)