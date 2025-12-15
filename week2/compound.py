p=float(input("enter principle"))
r=float(input("enter rate intrest"))
t=float(input("enter time(in years)"))
amount=p*(1+r/100)*r*t
ci=amount-p
print("compound interst=",ci)

