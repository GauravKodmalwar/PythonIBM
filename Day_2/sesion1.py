with open("IOFile", "r") as fileIO:
    print(fileIO.read())

print("*****************")
fileIO = open("IOFile", "r")
print(fileIO.read())

print("*****************")
fileIO = open("..\pythonIO.txt", "r")
print(fileIO.read())

varT="F:\PythonIBM\\"
print("*****************")
fileIO = open(varT + "pythonIO.txt", "r")
print(fileIO.read())



print("*****************")
fileIO = open(varT + "pythonIO.txt", "r+")
fileIO.write("Python " * 10)
fileIO.seek(0)
print(fileIO.read())

count = int(input("File size = "))
for i in range(count):
    temp = open("File" + str(i), "w")
    temp.write("Python is great langauge \n" * i)
    temp.close()







