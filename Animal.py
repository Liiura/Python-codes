class Animal:
    def __init__(self,code,weight,price,tipe,datebought):
        self.code=code
        self.weight=weight
        self.price=price
        self.tipe=tipe
        self.datebought=datebought
        self.datesell="null"
    def GetDateSell(self):
        return self.datesell
    def SetDateSell(self,datesell):
        self.datesell=datesell
    def GetDateBought(self):
        return self.datebought
    def SetDateBought(self,datebought):
        self.datebought=datebought
    def GetTipe(self):
        return self.tipe
    def GetCode(self):
        return self.code
    def GetWeight(self):
        return self.weight
    def GetPrice(self):
        return self.price
    def SetCode(self,code):
        self.code=code
    def SetWeight(self,weight):
         self.weight= self.weight+weight
    def SetPrice(self,price):
         self.price=price
class Chicken(Animal):
    def Chicken(self,type,age):
        self.type=type
        self.age=age
    def ToString(self):
        return print("""The animal has been bought with the parameters
        code=""",self.code,""" 
        weigh=""",self.weight,""" 
        price=""",self.price,""" 
        type""",self.type,"""
        age=""",self.age)
    def Information(self):
        return print("""
        animal=""",self.tipe,""" 
        code=""", self.code, """ 
        weigh=""", self.weight,"""
        price=""", self.price,"""
        type""", self.type,"""
        age=""",self.age)
    def GetType(self):
        return self.type
    def SetType(self,type):
        self.type=type
    def GetaAge(self):
        return self.age
    def SetType(self, age):
        self.age = age
class Pig(Animal):
    def Pig(self,sex):
        self.sex=sex
    def ToString(self):
        return print("""The animal has been bought with the parameters 
        code=""", self.code, """ 
        weigh=""", self.weight,""" 
        price=""", self.price,"""
        sex""", self.sex)
    def Information(self):
        return print("""
        animal=""",self.tipe,""" 
        code=""", self.code, """ 
        weigh=""", self.weight,"""
        price=""", self.price,"""
        sex""", self.sex)

    def GetSex(self):
        return self.sex
    def SetSex(self,sex):
        self.sex=sex
class Cow(Animal):
    def Cow(self,type):
        self.type=type
    def ToString(self):
        return print("""The animal has been bought with the parameters 
        code=""", self.code, """ 
        weigh=""", self.weight,""" 
        price=""", self.price,""" 
        type""", self.type)
    def Information(self):
        return print("""
        animal=""",self.tipe,""" 
        code=""", self.code, """ 
        weigh=""", self.weight,""" 
        price=""", self.price,""" 
        type=""", self.type)
    def GetType(self):
        return self.type

    def SetType(self, type):
        self.type = type