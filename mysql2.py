import mysql.connector as connection 

mydb= connection.connect(host ="localhost", user ="root", password ="lalaland@7680")
cursor=mydb.cursor()

q="insert into saurav.ineurotails value( 101 , 'sudh' , 'asdffasdfdg.gmail', 100 )"
cursor.execute(q)
mydb.commit()
cursor.execute("select * from saurav.ineurotails")
for i in cursor.fetchall():
    print(i)