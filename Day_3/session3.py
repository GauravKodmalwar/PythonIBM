import json

a = {"name": "John",
     "age": 31,
     "Salary": 25000}

fileOpen = open("JSON.json", "w+")
fileOpen.write(json.dumps(a))

fileOpen.seek(0)

print(json.load(fileOpen))
fileOpen.close()
