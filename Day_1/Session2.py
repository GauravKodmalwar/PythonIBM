variable_3 = 5
print(type(variable_3))

import gc
gc.collect()
print(gc.get_count())
print(gc.get_threshold())
gc.set_threshold(500, 5, 5)
print(gc.get_threshold())

a, b, c = 5, 7, 6
if(True):
    a, b, c = 5, 7, 6
    print(a, b, c)
a, b, c = 8, 20, 36
print(a, b, c)

#del a, b, c
#print(a, b, c)


xyz = '\u0365'
print("value of unicode is {} and type is {}".format(xyz, type(xyz)))

varList = [5, 10, 6]
print(min(varList))

#varList = [3, 65.2, 'akshay', 'sneha', 'deepika']
#print(varList)
varList.append(54)
varList.extend([56, 15, 66, 22])
varList[2] = 6666
print(varList)

varText = "Python Training"
print(id(varText))
print(len(varText))
varText = "Python Training"
print(varText)
print(id(varText))

varText2 = varText
print(id(varText2))
print(id(varText))

varText = "Python"
print(varText2)
print(id(varText2))
print(id(varText))

print(35355 not in varList)
print(varText2 is not varText)

print(varList[-3])

varTuple = (5, 2, 6, "Python")
print(varTuple)
#varTuple[2] = 45
z = (5, 6, 1)
print(z)
x = list(z)
print(x)

xyz = ([4, 6], "Python")
xyz[0].append(67)
print(xyz)
print(len(xyz[0]))