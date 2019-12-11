# Arithmetic Operators

a = 22
b = 7
print("********** arithmatic **********")
print("addition of two vars is ", a + b)
print("subtraction of two vars is ", a - b)
print("division of two vars is ", a/b)
print("multiplication of two vars is ", a*b)
print("remainder after division of two vars is ", a%b)
print("quotient after division of two vars is ", a//b)
print("power of one vars to another is ", a**b)
print("power of one var to other var is ", pow(a, b))

# Comparison (Relational) Operators
print("********** Comparison or Relational **********")
print("is True == True, ", True==True)
print("is True != False, ", True!=False)
print("is 5 > 3, ", a > b)
print("is 5 < 3, ", a < b)
print("is 5 >= 3, ", a >= b)
print("is 5 <= 3, ", a <= b)

print("********** Assignment Operators **********")
a = b + 5
a /= 2
b *= 1
a //= 2
b **= 3
b //= a
a %= b
print(a, b)

#print("power of one no to other = ", int(input())**int(input()))

print(bin(22))
print("********** Bitwise Operators **********")
a = 13 #0b00111100
b = 60 #0b00001101
print(bin(22))

print("binary AND operator", a&b)
print("binary OR operator", a|b)
print("binary XOR operator", a^b)
print("binary negate or flipping bits operator", ~a)
print("binary left shift", a << 2)
print("binary right shift", b >> 2)

print("********** Logical Operators **********")
print(b > 4 and a < 2)
print(b or a)
print(not(a and b))

if a > b:
    print("{} is a big number".format(a))
    print()
elif a==b:
    print("{} number is same as {}".format(a, b))
else:
    print("{} is a small number".format(a))

if(True):
    print()
else:
    pass

if(type("asdfsd") == str):
    print("passed")

c = a if a > b else b
print(c)

a = 60
b = 15

print( (b, a) [a < b] )
print({False: b, True: a} [a < b])
print("Both a and b are equal" if a == b else "a is greater than b"
        if a > b else "b is greater than a")

varList = [3, 5, 8 , 10]
for i in varList:
    print(i)

for i in range(1, 5):
    print(i)

for i in range(len(varList)):
    print(varList[i])

i = 1
while i < 15:
    print(" "*(15 - int(i/2)) + "*"*i)
    i += 2

print("continue and break")
for i in varList:
    if( i > 5):
        break
    print(i)

# Write a fibonacii number up to a largest number

a = int(input("Enter larget number = "))
b, c = 0, 1
temp = []
for i in range(1, int(a/2)):
    temp.append(b + c)
    b += c
    c = b + c
    if(temp[-1] > a):
        temp.pop()
        break
print(temp)