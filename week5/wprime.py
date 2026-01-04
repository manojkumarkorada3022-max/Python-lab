def prime(n, i):
    if i == n:
        return True
    if n % i == 0:
        return False
    return prime(n, i + 1)

n = int(input("Enter number: "))

if n > 1 and prime(n, 2):
    print("Prime")
else:
    print("Not Prime")
