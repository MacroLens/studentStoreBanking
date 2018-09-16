import gspread #google sheets API interfacing
from oauth2client.service_account import ServiceAccountCredentials #apparently a credential thing
import serial #arduino communication
import time
arduino = serial.Serial('COM6', 115200, timeout=.1) # python scripts now reads from the serial monitor at 115200 baud rate, COM6 is the port
scope = ['https://spreadsheets.google.com/feeds'] #copied, dont know what it does
creds = ServiceAccountCredentials.from_json_keyfile_name('nfcBank.json', scope)#copied, authenticate the email account with
client = gspread.authorize(creds) #copied
sheet = client.open_by_url('https://docs.google.com/spreadsheets/d/15OAWhKiOtsp_egQkNK727qk_KRxR_pPWd7QZ8ivnBuY/edit#gid=0').sheet1 #copied

while True: #infinite loop
        print('Place a card on the reader')
        #testing = sheet.get_all_records() #this was to see all the data in google sheets
        idNum = (arduino.readline().decode().strip()) #the .strip() gets rid of the \r\n new line characters
                                                          #the .decode(gets rid of the b'#########' and only leaves the content) || I don't know - Stack Overflow
        s = (''.join(x for x in idNum if x.isdigit())) #parse for the ID num || I don't know i copied stack overflow
        if idNum: #black-magic it runs // Help me please
                try:
                        cell = sheet.find(s) #finds the cell matching the ID & creates a cell object
                        name = (sheet.cell(cell.row, 1).value) #pull the name from the row
                        money = (int)(sheet.cell(cell.row, 3).value) #pull the cents from the row
                        result = money # used to compute math later
                        print(name, 'has ',money, 'cents.')
                        print('Enter Amount to remove in negative cents: ')
                        difference = (int)(input()) #Value to change positive or negative
                        if ((difference) <= money):
                                result = (money - difference) #Computes the math
                                sheet.update_cell(cell.row, 3, result) #update cell to have new value
                                time.sleep(4)
                                result = sheet.cell(cell.row, 3).value #debug - returns new value
                        else:
                                print('Balance too low.')
                        print(name, 'has ',result, 'cents.') #debug - prints new value
                except:
                        print('No account. Make new account? \'Yes\' or \'No\'')
                        if input()=='Yes':
                                print('What\'s the name?')
                                newName = input()
                                print('Add balance? \'Yes\' or \'No\'')
                                if input()=='Yes':
                                        print('How much in cents?')
                                        newBal = (int)(input())
                                else:
                                        newBal = 0
                                myList = [newName, (int)(idNum), newBal]
                                print(myList)
                                sheet.append_row(myList)
                        else:
                                print('testno')
                        

#print(testing)
#print(cellFind)
