# print(5+1)
# n=(5+1)
# print(n)

# d1=("6"+"1")
# print(d1)


# def add(x, y, z = 0): 
#     return x + y+z
# print(add(2, 3))
# print(add(2, 3, 4)

# def names(a,b,c):
#     n=a*b*c
#     print(n)5
# names(4,5,5)

# class Animal:
#     def sound(self):
#         return("animal sound")
# class Dog(Animal): 
#     def sound(self):
#         print("Dog barks")
#         print("Animal makes a sound")
# animal = Animal()
# dog = Dog()
# animal.sound()
# dog.sound()

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
# x=dog("bark","white")
# y=cat("meow","brown")
# x.printname()
# y.printname()
    
# class store:
#     def __init__(self,price,name):
#         self.price=price
#         self.name=name
#     def printname(self):
#         print(self.price,self.name)
# class books(store):
#     pass
# x=store("ABCD",567)
# x.printname()

class employee:
    def __init__(self,name,salary):
        self._name = name
        self._salary = salary
    def _display(self):
        print("name:", self._name)
        print("salary:", self._salary)
class trainer(employee):
    def __init__(self,name,salary,age):
        super().__init__(name, salary)
        self.age = age
    def display(self):
        self._display()
        print("age:", self.age)
x = trainer("Divya", 2000000, 21)
x.display()


