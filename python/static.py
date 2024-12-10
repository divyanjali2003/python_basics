class maths():
    @staticmethod
    def addNum(num1,num2):
        return num1+num2
if __name__=="__main__":
        res=maths.addNum(1,2)
        print("the result is", res)

# class person:
#     def __init__ (self,name,age):
#         self.name=name
#         self.age=age
#     @staticmethod
#     def isAdult(age):
#         return age >18
# if __name__ =="__main__":
#     res =person.isAdult(12)
#     print("is person adult:",res)
#     res=person.isAdult(22)
#     print("/n is person adult:",res)

# class person:
#     age=25
#     def printAge(cls):
#         print("the age is:",cls.age)
# person.printAge=classmethod(person.printAge)
# person.printAge()

# from datetime import date
# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     @classmethod
#     def fromBirthyear(cls,name,year):
#         return cls(name,
#                    date.today().year-year)
#     @staticmethod
#     def isAdult(age):
#         return age>18
# person1=person("Divya",21)
# person2=person.fromBirthyear("Divya",2003)
# print(person1.age)
# print(person2.age)
# print(person.isAdult(22))