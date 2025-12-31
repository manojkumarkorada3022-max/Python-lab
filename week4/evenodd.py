n=int(input("enter how many numbers:"))
even=0
odd=0
for i in range(n):
    num=int(input("enter a number:"))
    if num%2==0:
        even=even+1
    else:
        odd=odd+1
print("even=:",even)
print("odd=:",odd)