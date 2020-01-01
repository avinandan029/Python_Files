import sqlite3
class DataBase:
    def connect(self):
        self.db=sqlite3.connect('STUDENTDB')
        return self.db
    def disconnect(self):
        self.db.close()
    def Createtable(self):
        sql_smt=''' Create table Students( StudentNo 
        int Primary key, Name Text,Department Text,location Text)'''
        result=self.db.execute(sql_smt)
        self.db.commit()
        return result
    #print("database created")
    def inserttable(self,Sid,Sname,Dept,Loc):
        sql_smt='''insert into Students values (1,'Avinandan','CSE','PATNA'),
        (2,'bittu','mech','ara')''',(Sid,Sname,Dept,Loc)
        result = self.db.execute(sql_smt)
        self.db.commit()
        return result
        print("data insert")
    def readtable(self):
        sql_smt=''' select * from Students '''
        result = self.db.execute(sql_smt)
        self.db.commit()
        return result
        print(("data base read"))






db_obj1=DataBase()
db_obj1.connect()
#db_obj1.Createtable()
#db_obj1.inserttable()
res=db_obj1.readtable(111)
for i in res:
    print(i)
db_obj1.disconnect()
