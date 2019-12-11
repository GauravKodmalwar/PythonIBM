import string
import random
import secrets

print("".join(secrets.choice(string.ascii_uppercase + string.digits) for i in range(15)))

print(''.join(random.choices(string.ascii_uppercase + string.digits, k= 10)))
res = ''.join(secrets.choice(string.ascii_uppercase + string.digits) for i in range(15))
print(res)

varList = ["Python", " Day 1", " Day 3"]
xyz = '***'.join(varList)
print(xyz)

print(xyz.split(" "))
print(xyz.find(" Day34"))
print(xyz.replace(" ", "$$$$$"))

print(int("010111", 2))

name, age = "John", 23
print("%s is %d years old." % (name, age))
tokens = [2, 4, 6, 9]
print("Tokens are %s" % tokens)

print(f"{name} is {age} years old.")

varText2 = "Hello, Python training started"
print(varText2[::-1])

for i,v in enumerate(xyz):
    print(f'value at position {i} is {v}')

thistuple = (1)
print(type(thistuple))

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

thistuple = (("apple", "banana", "cherry"), ("apple", "banana", "cherry"))
print(thistuple[-1][::2])

a = (3, 56, 20, 10)
b = (12.4, 567.2, 565.357)
print("addition of tuples ", a + b)
print("multiplication of tuples ", a * 5)
print("smalles number in tuple: ", min(b))