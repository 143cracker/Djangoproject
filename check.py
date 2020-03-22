import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",passwd="root",database="shivam")
cursor=con.cursor()
cursor.execute("select * from book_time")
data=cursor.fetchall()
for row in data:
    print(row)
