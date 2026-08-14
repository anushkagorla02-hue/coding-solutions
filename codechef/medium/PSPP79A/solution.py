def compute_value(a, b):
    # update your code below this line
    print(a**2+2*a*b+b**2)
    print(a+b)
    
    
    

t = 3
for _ in range(t):
    A, B = map(int, input().split())
    compute_value(A, B)
