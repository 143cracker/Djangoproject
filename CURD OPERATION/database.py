import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",passwd="root",database="shivam")
cursor=con.cursor()
cursor.excute(create table book_time(Title varchar(25),Author varchar(25),Mobile_No int,Email varchar(25)));


