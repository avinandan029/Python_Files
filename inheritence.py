# class BC:
#     def __init__(self,x,y):
#         self.a=x
#         self.b=y
#     def DisplayBC(self):
#         print("A value is :",self.a)
#         print("B value is :",self.b)
# class DC(BC):
#     def __init__(self,m,n):
#         super().__init__(10,20)
#         self.i=m
#         self.j=n
#     def DisplayDC(self):
#         super().DisplayBC()
#         print("I value is :",self.i)
#         print("J value is : ",self.j)
# class TC(DC):
#     def __init__(self,q,r):
#         super().__init__(100,200)
#         self.o=q
#         self.p=r
#     def DisplayTC(self):
#         super().DisplayDC()
#         print("O value is :",self.o)
#         print("P value is :",self.p)
#
# ojb=TC(1000,2000)
# ojb.DisplayTC()
#
#
#
#
'''Multipath inheritence Example'''
class BC:
    def __init__(self,x,y):
        self.a=x
        self.b=y
    def DisplayBC(self):
        print("A value is :",self.a)
        print("B value is :",self.b)
class DC(BC):
    def __init__(self,m,n):
        BC.__init__(self,10,20)
        self.i=m
        self.j=n
    def DisplayDC(self):
        print("I value is :",self.i)
        print("J value is : ",self.j)
class TC(B):
    def __init__(self,q,r):
        BC.__init__(self,10,20)
        DC.__init__(self,100,200)
        self.o=q
        self.p=r
    def DisplayTC(self):
        BC.DisplayBC()
        DC.DisplayDC()

        print("O value is :",self.o)
        print("P value is :",self.p)
ojb=TC(1000,2000)
ojb.DisplayTC()



