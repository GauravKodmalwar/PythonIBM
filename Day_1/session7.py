varSet = {4, 5, 6, 7,3, 2, 4, 5, 7, 2}

print(varSet)

varSet2 = varSet.copy()
#for i in [5, 7, 100, 105]:
#    varSet.add(i)
varSet2 = [varSet.add(i) for i in [5, 7, 100, 105]]
print(varSet2)
print(id(varSet), id(varSet))

varList = [5, 6, 7]
[varSet.add(i) for i in varList]
print(varSet)

print([i for i in varList])

dict2 = {"python": 25, "Day 2": 39, "Day3": 20, "python": 30}
print(dict2)

print(dict2.get("python"))
print(dict2.values())
print(dict2.keys())

dict2["python25"] = 100
print(dict2)
"""
dict3 = {}
count = input("Size of the dictionry = ")

dict3["python " + str(i)] = [i for i in range(int(count))]

print(dict3)
"""
for x, y in dict2.items():
  print("key is {} and value is {}".format(x, y))

if "python" in dict2.keys():
    print("Passed")