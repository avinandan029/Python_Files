import sqlite3
class DataBaseOperations:

    def connect(self):
        self.db = sqlite3.connect('SBIDB')
        return self.db
    def disconnect(self):
        self.db.close()
    def createTbl(self):
        sql_smt=''' create table Accounts (AccountNo int PRIMARY KEY,NAME text not null,
        Type text not null,
        Balance real not null) 
        '''
        res=self.db.execute(sql_smt)
        self.db.commit()
        return res
    def insertTbl(self,id_val):
        sql_smt='''insert into Accounts values(%s, 'Avinandan','Saving',20000.00)'''%(id_val)
        res = self.db.execute(sql_smt)
        self.db.commit()
        return res
    def readTbl(self):
        sql_smt=''' select * from Accounts '''
        res = self.db.execute(sql_smt)
        self.db.commit()
        return res
db_obj1= DataBaseOperations()
db_obj1.connect()
#db_obj1.createTbl()
db_obj1.insertTbl("112")
output=db_obj1.readTbl()
for i in output:
    print(i)
db_obj1.disconnect()