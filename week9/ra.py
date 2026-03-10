import random
with open("random_numbers.txt", "w") as file:
   for i in range(20):
       num = random.randint(1,100)
       file.write(str(num) + "\n")
print("20 random numbers written to random_numbers.txt")
