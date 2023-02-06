import mysql.connector as conn

mydb=conn.connect(host="localhost", user ="root", passwd ="mysql")
cursor=mydb.cursor()


cursor.execute("select * from ravi.emp_details where city='Tumkur'")

for i in cursor.fetchall():
    print (i)
