# cook your dish here
a=input()
l="aeiou"
count=0
i=0
while i<len(a):
    if a[i] in l:
        count+=1
    i+=1
print(count)
