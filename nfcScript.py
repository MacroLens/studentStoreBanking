#!/usr/bin/python3
import subprocess
import mysql.connector
#operations and needed test variables
table='ids'
owner='id_owner'
idUID='id_UID'
balance='id_balance'
newName=None
newBal=None
UID=None
def select(UID):
    return f"SELECT * FROM {table} WHERE {idUID} = {UID}"
def update(newBal, UID):
    return f"UPDATE {table} SET {balance} = {newBal} WHERE {idUID} = {UID}"
def insert(newName, UID, newBal):
    return f"INSERT into {table} ({owner},{idUID},{balance}) VALUES ({newName}, {UID}, {newBal})"


def decode():
    output = open('output', 'w+'); # Check for output file, if none make one and give write privielges.
    try:
        var = subprocess.check_output('./chip_reader').decode('utf-8').strip(); # declare variable var, read the output of quick_start_example1 script and decode it from the UTF-8 format and strip it of any extra trailing characters like line breaks
        hex_list = var.split(); # takes the string, splits it by spaces, and makes it into a list
        for x in range(len(hex_list)): # for every hex number in the list go through it and turn it into a decimal interger
            hex_list[x] = int(hex_list[x], 16) # converts Hexidecimal to decimal so it's easy to mess with.
        nfcUID = hex_list[3]; # Creating a unique code to identify a card, take the decimals and bitshift them around
        nfcUID <<= 8; nfcUID |= hex_list[2]; # Shift left 8 bits, += the third decimal
        nfcUID <<= 8; nfcUID |= hex_list[1]; # etc
        nfcUID <<= 8; nfcUID |= hex_list[0]; # etc
        #print(nfcUID)
        #print(hex_list)
        output.write(str(nfcUID)); # Writes to the output file the nfcUID
    except (OSError, subprocess.CalledProcessError) as e:
        print(e)
        #print("error: may not be able to read card. check card reader connection")
    return str(nfcUID)
def sql():
    print("Place Card on Reader:")
    UID = decode()
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
    mycursor.execute(select(UID))
    myresult=mycursor.fetchone() #always returns a list of what was found
    if not myresult:    #if the list is emtpy
        print('No Results. Create an account? Y/N:');
        if input()=="Y":
            print('What\'s the name?')
            newName = "'"+input()+"'"
            print('Add balance? \'Yes\' or \'No\'')
            if input()=='Yes':
                print('How much in XX.XX?')
                newBal = (float)(input())
            else:
                newBal = 0
            mycursor.execute(insert(newName, UID, newBal))
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
            mycursor.execute(update(newBal, UID))  # update cell to have new value
            mydb.commit()
            mycursor.execute(select(UID))  # debug - returns new value
            myresult=mycursor.fetchone()
            print(myresult)
        else:
            print('Balance too low.')
    #mycursor.execute(update)
    mydb.commit();




