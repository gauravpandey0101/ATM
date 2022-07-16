import mysql.connector as atm
object=atm.connect(host='localhost',user='root',password='rekhagaurav123@',database='atm')
print("Conect Success")
object1=object.cursor()

object1.execute('create table if not exists ATM (name varchar(20),password varchar(20))')


object.commit()
object.close()
print('DBMS INSERT VALUE SUCCESS')