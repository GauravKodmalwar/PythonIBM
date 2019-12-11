varList = [2, 5, 7, 8, 9, 10]
print(varList.pop(3))
print(varList)

for i in zip(varList):
    print(i)

print("addition in list ", varList + [5])
print("multiplication in list ", varList * 2)

print(varList[3:6:2])

# get an iterator using iter()
my_iter = iter(tuple((5, 6, 8)))
# fetch next value from iterator using next
print(next(my_iter))

varList = [[5, 6, 7, 8], [5, 6, 7, 8]]
print(varList)
for i in range(len(varList)):
    for k in range(len(varList[i])):
        varList[i][k] *= 2

print(varList)

varList2 = [15, 26, 37, 5, 46, 57, 86]
varList3 = [i * 2 for i in varList2 if i%2 == 0]
varList4 = [i * 2 if i%2 == 0 else i for i in varList2]

varList3, varList4 = [i for i in varList2 if i%2 == 0], [i for i in varList2 if i%2 != 0]
print(varList3, varList4)

varText = ["Python", "2", "Training", "Progress"]
print(" ".join(varText))

print([i for i in varText if i.isdigit()])

import time

start = time.time()
print([i for i in range(10000)])
end = time.time()

print(end - start)