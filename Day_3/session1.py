import mysql.connector

mydb = mysql.connector.connect(
host="localhost",
username="python",
passwd="python",
database="PythonTraining"
)

mydb.connect()
mycursor = mydb.cursor()

"""
for i in varTableNames:
    mycursor.execute("DROP TABLE {}".format(i[0]))
"""
for i in range(5):
    mycursor.execute("drop table customers_{}".format(i))
    mycursor.execute("CREATE TABLE customers_{} (name VARCHAR(255), address VARCHAR(255))".format(i))
    for k in range(i*5):
        sql = """INSERT INTO customers_{} 
        (name, address) VALUES (%s, %s)""".format(i)
        val = ("Name {}".format(k), "Highway {}".format(k))
        mycursor.execute(sql, val)

mycursor.execute("show tables")
print(mycursor.fetchall())

for i in range(5):
    mycursor.execute("select * from customers_{}".format(i))
    values = mycursor.fetchall()
    print(values)

mydb.commit()
#mydb.rollback()

mycursor.close()
mydb.close()