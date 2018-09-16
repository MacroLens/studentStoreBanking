import mysql.connector
mydb = mysql.connector.connect(
        host='192.168.1.131',
        user='test',
        password='test123',
        database='nfc'
        )
mycursor = mydb.cursor()
mycursor.execute("SELECT * from ids")
for x in mycursor:
    print(x)

