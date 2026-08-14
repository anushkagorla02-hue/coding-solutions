# Update the function below
def calculator(num1, num2, operator):
    if operator=='+':
        print(num1+num2)
    elif operator=='-':
        print(num1-num2)
    elif operator=='*':
        print(num1*num2)
    elif operator=='/':
        if num2==0:
            print("Cannot divide by zero")
        else:
            print(num1/num2)
    
num1, num2 = map(int, input().split())
operator = input()
calculator(num1, num2, operator)