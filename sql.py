import mysql.connector
#Connect to the mysql server
mydb = mysql.connector.connect(
        host='192.168.1.135',
        user='test',
        password='test123',
        database='nfc'
        )

#lets me execute things
mycursor = mydb.cursor()
#Run any mysql command like this
mycursor.execute("SELECT * from ids WHERE id_owner = 'Ded man'")
myresult=mycursor.fetchall() #always returns a list of what was found
if not myresult:    #if the list is emtpy
    print('No Results. Create an account?');
else:
    for x in myresult:
        print(x)
