import mysql.connector
#operations and needed test variables
UID=(int)(open('output').read())
table='ids'
owner='id_owner'
idUID='id_UID'
balance='id_balance'
newName=None
newBal=None
select=f"SELECT * FROM {table} WHERE {idUID}={UID}"
insert=f"INSERT into {table} ({owner},{idUID},{balance}) VALUES ({newName}, {UID}, {newBal})"
#this is a function due to instancing issues I was facing
def update():
        return f"UPDATE {table} SET {balance} = {newBal} WHERE {idUID} = {UID}"
#Connect to the mysql server
mydb = mysql.connector.connect(
        host='192.168.1.135',
        user='test',
        password='test123',
        database='nfc'
        )
#lets me execute things on the database
mycursor = mydb.cursor()
# Database: nfc; Table: ids
# id_owner | id_uid | id_balance
#Return the row where the owner is Dylan Le
mycursor.execute(select)
myresult=mycursor.fetchone() #always returns a list of what was found
if not myresult:    #if the list is emtpy
    print('No Results. Create an account? Y/N:');
    if input()=="Y":
        print('What\'s the name?')
        newName = input()
        print('Add balance? \'Yes\' or \'No\'')
        if input()=='Yes':
            print('How much in XX.XX?')
            newBal = (float)(input())
        else:
            newBal = 0
        mycursor.execute(insert)
    else:
        print('ok')
else:
        name=myresult[0]
        money= float(myresult[2])
        print(f"{name} has ${money}.")
        print('Enter Amount to remove in negative $: ')
        difference = (float)(input())  # Value to change positive or negative
        if (difference * -1) <= money:
                newBal = (money + difference)  # Computes the math
                mycursor.execute(update())  # update cell to have new value
                mydb.commit()
                mycursor.execute(select)  # debug - returns new value
                myresult=mycursor.fetchone()
                print(myresult)
        else:
                print('Balance too low.')
#mycursor.execute(update)
mydb.commit();
