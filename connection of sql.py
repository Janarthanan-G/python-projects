import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Janarthanan@1812",
    database='EMPLOOYES'
)
print(db)
mycursor =db.cursor()

#CREATE DATABASE:
#mycursor.execute("CREATE DATABASE EMPLOOYES")

#CREATE TABLE:
#mycursor.execute("CREATE TABLE WORKS_DETAILS(EMPLOYEE_ID INT,NAME VARCHAR(50),PHONE_NO INT,MAIL_ID VARCHAR(70),ADDRESS VARCHAR(210))")

#INSERT VALUE INTO TABLE:
#SQL="INSERT INTO WORKS_DETAILS (EMPLOYEE_ID,NAME,PHONE_NO,MAIL_ID,ADDRESS)VALUES(%s,%s,%s,%s,%s)"
#VALUE=(20210,'JANARTHANAN',1231231234,'janarthanan@gmail.com','ABCD COLONY')
#mycursor.execute(SQL,VALUE)
#db.commit()

#CRAETE MANY VALUES:
#VALUE=[(20211,'KRISHNA',1234563,'krishna@gmail.com','EFGH STREET'),(20212,'DHARANRAJ',141563,'dharanraj@gmail.com','IJKL WEST'),(20213,'PAVIN',544236,'pavin@gmail.com','MNOP COLONY'),(20214,'HARI',721254,'hari@gmail.com','QURST STREET')]
#mycursor.executemany(SQL,VALUE)
#db.commit()

#GET ALL VALUES:
#SQL="SELECT * FROM WORKS_DETAILS"
#mycursor.execute(SQL)
#result=mycursor.fetchall()
#for i in result:
#    print(i)

#UPDATE METHOD:
#SQL="UPDATE WORKS_DETAILS SET NAME='HARIPRASANNA' WHERE NAME='HARI'"
#mycursor.execute(SQL)
#db.commit()

#DELETE METHOD:
#SQL="DELETE FROM WORKS_DETAILS WHERE NAME='HARIPRASANNA'"
#mycursor.execute(SQL)
#db.commit()

#ORDERBY METHOD:
SQL="SELECT * FROM WORKS_DETAILS ORDER BY NAME ASC"
mycursor.execute(SQL)
result=mycursor.fetchall()
for i in result:
    print(i)


