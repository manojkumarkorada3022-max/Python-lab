file = open("sample.txt", "w")
file.write("hello manoj\n")
file.write("welcome to python\n")
file.close()

file=open("sample.txt","r")
print("using read()")
print(file.read())
file.close()

file = open("sample.txt", "r")
print("using readline()")
print(file.readline())
file.close()

file = open("sample.txt", "r")
print("using readlines()")
print(file.readlines())
file.close()
