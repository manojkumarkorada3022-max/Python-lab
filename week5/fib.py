def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
n = int(input("enter numbers of terms:"))
a = 0
b = 1
print("using itration:")
for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
print()
print("using recursion:")
for i in range(n):
    print(fib(i), end=" ")