# class person:
#     def __init__(self,fname,lname):
#         self.fname=fname
#         self.lname=lname
#     def printname(self):
#         print(self.fname,self.lname)
# x=person("john","doe")
# x.printname()

# class name:
#     def __init__(self,fname,lname):
#         self.fname=fname
#         self.lname=lname
#     def printname(self):
#         print(self.fname,self.lname)
# x=name("Divya","Dileep")
# x.printname()

# class name:
#     def __init__(self,fname,lname):
#         self.fname=fname
#         self.lname=lname
#     def printname(self):
#         print(self.fname,self.lname)
#         class student(name):
#             pass
# x=name("Divya","Dileep")
# x.printname()

# class animal:
#     def __init__(self,sound,colour):
#         self.sound=sound
#         self.colour=colour
#     def printname(self):
#         print(self.sound,self.colour)
# class dog(animal):
#     pass
# class cat(animal):
#     pass
# x=dog("barck","white")
# y=cat("meow","brown")
# x.printname()
# y.printname()

# class person:
#     def __init__(self,fname,lname):
#         self.fname=fname
#         self.lname=lname
#     def printname(self):
#         print(self.fname,self.lname)
# class student(person):
#         def __init__(self, fname, lname):
#             super(). __init__(fname,lname)
# x=student("Divya","Dileep")
# x.printname()

# class animal:
#     def __init__(self,colour,sound):
#         self.colour=colour
#         self.sound=sound
#     def printname(self):
#         print(self.colour,self.sound)
# class dog(animal):
#     def __init__(self, colour, sound):
#         super().__init__(colour, sound)
# class cat(animal):
#     def __init__(self, colour, sound):
#         super().__init__(colour, sound)
# x=dog("White","Brack")
# y=cat("brown","meow")
# x.printname()
# y.printname()        

class company:
    def __init__(self,sal,exp):
        self.salary=sal
        self.experience=exp
    def printname(self):
        print(self.salary,self.experience)
class employe(company):
      pass
x=employe(25000,"2 years")
x.printname()  
