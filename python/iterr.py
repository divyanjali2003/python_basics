# # define a list
# my_list = [4, 7, 0,8,90,23]

# # create an iterator from the list
# iterator = iter(my_list)

# # get the first element of the iterator
# print(next(iterator))  # prints 4

# # get the second element of the iterator
# print(next(iterator))  # prints 7

# # get the third element of the iterator
# print(next(iterator))  # prints 0

# print(next(iterator))

# my_list=[4,5,9]
# iterator=iter(my_list)
# print(next(iterator))
# print(next(iterator))
# print(next (iterator))

# my_numbers=[2,4,6,8,10]
# company=iter(my_numbers)
# print(next(company))
# print(next(company))
# print(next(company))
# print(next(company))
# print(next(company))

# class mynumbers:
#     def __iter__(self):
#         self.a=1
#         return self
#     def __next__(self):
#         x=self.a
#         self.a += 1
#         return x
# myclass=mynumbers()
# myiter=iter(myclass)
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

# class mynames:
#     def __iter__(self):
#         self.b=1
#         return self
#     def __next__(self):
#         x=self.b
#         self.b += -5
#         return x
# myworks=mynames()
# myiter=iter(myworks)
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

# from abc import ABC, abstractmethod
# class polygon(ABC):
#     @abstractmethod
#     def noofsides(self):
#         pass
# class triangle(polygon):
#     def noofsides(self):
#         print("i have 3 sides")
# class pentagon(polygon):
#     def noofsides(self):
#         print("i have 5 sides")
# class hexagon(polygon):
#     def noofsides(self):
#         print("i have 4 sides")
# r=triangle()
# r.noofsides()
# k=pentagon()
# k.noofsides()
# a=hexagon()
# a.noofsides()

# from abc import ABC, abstractmethod
# class animal(ABC):
#     def move(self):
#         pass
# class human(animal):
#     def move(self):
#         print("i can walk and run")
# class snake(animal):
#     def move(self):
#         print("i can crawl")
# class dog(animal):
#     def move(self):
#         print("i can bark")
# class lion(animal):
#     def move(self):
#         print("i can roar")
# r=human()
# r.move()
# k=snake()
# k.move()
# s=dog()
# s.move()
# y=lion()
# y.move()

# from abc import ABC , abstractmethod
# class avengers(ABC):
#     def strength(self):
#         pass
# class captain_america(avengers):
#     def strength(self):
#         print("strength lvel is 65/100")
# class iron_man(avengers):
#     def strength(self):
#         print("strength level is 75/100")
# class thor(avengers):
#     def strength(self):
#         print("sterngth level is 95/100")
# class hulk(avengers):
#     def strength(self):
#         print("strength level is88/100")
# c=captain_america()
# c.strength()
# i=iron_man()
# i.strength()
# t=thor()
# t.strength()
# h=hulk()
# h.strength()

from abc import ABC, abstractmethod
class car(ABC):
    def milege(self):
        pass
class tesla(car):
    def milege(self):
        print("the milege is 30kmph")
class suzuki(car):
    def milege(self):
        print("the milege is 25kmps")
class duster(car):
    def milege(self):
        print("the milege is 27kmph")
t=tesla()
t.milege()
r=suzuki()
r.milege()
f=duster()
f.milege()
