s=input("enter string:")
count=0
for ch in s:
    if ch in 'abcdefghijklmnopqrstuvwxyz':
        count=count+1
print("number of lower case characters:",count)