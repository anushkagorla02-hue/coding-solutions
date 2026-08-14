def password_validator(password):
    # complete the function 
    if len(password)<8:
        return False
    hasupper=False
    hasdigit=False
    for char in password:
        if char.isupper():
            hasupper=True
        if char.isdigit():
            hasdigit=True
    if hasupper and hasdigit:
        return True
    else:
        return False
    
    
    

password = input()
result = password_validator(password)
print(result)