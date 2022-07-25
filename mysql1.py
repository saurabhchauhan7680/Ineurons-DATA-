import mysql.connector as connection 

mydb= connection.connect(host ="localhost", user ="root", password ="lalaland@7680")
cursor=mydb.cursor()
#cursor.execute("create database saurav")
#q1=cursor.execute("create table saurav.ineurotails( employee_id int(10) , employee_name varchar(88) , employee_mailid varchar(88) , emp_salary int(10) )")

q2=cursor.execute("select * from saurav.ineurotails")
print(q2)