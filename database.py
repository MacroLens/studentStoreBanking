#!/usr/bin/python3
import mysql.connector

class database:
    def __init__(self):
        self.database = mysql.connector.connect(
            host='localhost',
            user='storeOperator',
            password='storePassword',
            database='Store'
        )
        self.cursor = self.database.cursor()

    def __callProcedure(self, procedureName, args):
        result = self.cursor.callproc(procedureName, args)
        # Any changes need to be committed.
        self.database.commit()
        return result  # returns a tuple with data from procedure call.

    def getBalance(self, id):
        return self.__callProcedure("GetBalance", (id, 0, 0))[-2:]  # The procedure returns on zeros. Balance, Processed?

    def getStudentName(self, id):
        return self.__callProcedure("GetStudentName", (id, 0, 0))[-2:]  # Name, Processed?

    def changeBalance(self, id, difference):
        return self.__callProcedure("ChangeBalance", (id, difference, 0))[-1:]  # Processed?

    def addAccount(self, id, name, balance):
        return self.__callProcedure("AddAccount", (id, name, balance, 0))[-1:]  # Processed?

    def closeConnection(self):
        self.cursor.close()  # close the connections
        self.database.close()




