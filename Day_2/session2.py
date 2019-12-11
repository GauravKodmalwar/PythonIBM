def processText(count, randomtext, greet="Hello"):
    return greet + "," + randomtext*int(count)

print(processText(randomtext= "Pythoner ", count=10))

def processText(count):
    return "Made a mistake \n"*count

print(processText(count=5))

x = lambda a, b: a+b
print(x(6, 5))

a = [5, 1]
xy = lambda a: a*2
print(xy(a))

#temp = None
def addition(a, b):
    global temp
    temp = a+b
    return temp

addition(5, 6)
print(temp)

xyz = lambda a: [i for i in range(a)]
print(xyz(5))


def multiArguments(*params):
    temp = []
    print(type(params))
    for i in params:
        temp.append(i)
    return " ".join(temp)

print(multiArguments("Hi ", "How are you?", " Had a good lunch"))


def multiArguments2(**params):
    temp = {}
    print(type(params))
    for i, k in params.items():
        temp[i] = k
    return temp

print(multiArguments2(var1 = "Hi ", var2 = "How are you?", var3 = " Had a good lunch"))

print("*****************")


def myFun(arg1, arg2, arg3):
  print("arg1:", arg1)
  print("arg2:", arg2)
  print("arg3:", arg3)

args = ("Geeks", "for", "Geeks")
myFun(*args)

temp = "Python"

import CONSTANTS

print(CONSTANTS.PI)
print(CONSTANTS.NO_Of_Days)

print(id(CONSTANTS.PI))
print(CONSTANTS.PI)
CONSTANTS.PI = 20
print(CONSTANTS.PI)
print(id(CONSTANTS.PI))


import sys
del sys.modules['CONSTANTS']
import CONSTANTS
print(CONSTANTS.PI)
print(id(CONSTANTS.PI))
