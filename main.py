import mysql.connector as conn

mydb=conn.connect(host="localhost", user ="root", passwd ="mysql")
print(mydb)
print("connection established")
cursor=mydb.cursor()
cursor.execute("show databases")
