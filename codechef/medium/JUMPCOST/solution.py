# cook your dish here
t=int(input())
arr=[]
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    for i in range(1,n):
        for j in range(i):
            pos=a[i]-(i+1)+(j+1)
            try:
               if a[pos]:
                  arr.append(pos)
            except(IndexError):
                arr=[]
    print(len(arr))               