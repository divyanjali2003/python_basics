# def my_decorator(func):
#     def inner():
#         print("i got decorated")
#         func()
#     return inner
# @my_decorator
# def ordinary():
#     print("i am ordinary")
# ordinary()

# def my_decor(func):
#     def inner():
#         print("i am divya")
#         func() 
#     return inner
# @my_decor
# def ordinary():
#     print("i have 2 books")
# ordinary()

# def my_device(func):
#     def inner(a,b):
#         print("i am going to divide",a,"and",b)
#         if b==0:
#             print("whoops! cannot divide")
#             return
#         return func(a,b)
#     return inner
# @my_device
# def device(a,b):
#     print(a/b)
# device(2,5)
# device(2,0)
    
# def my_divide(func):
#     def inner(x,y):
#         print("my work time",x,"and",y)
#         if y==3:
#             print("we can divide")
#             return
#         return func(x,y)
#     return inner
# @my_divide
# def divide(x,y):
#     print(x/y)
# divide(2,5)      
# divide(4,3)

# class myclass:
#     x=5
#     y=4
# p1=myclass()
# print(p1.x)
# p2=myclass()
# print(p2.x)

# class my_work:
#     a=6
#     b=7
# cl1=my_work() 
# print(cl1.a)
# cl2=my_work()
# print(cl2.b)

# class animal:
#     sound1="brack"
#     sound2="meow"
# d2=animal()
# print(d2.sound1)
# print(d2.sound2)

# class names:
#     name1="divya"
#     name2="dileep"
# n2=names()
# print(n2.name1)
# print(n2.name2)       

# class fruits:
#     fruits1="apple"
#     fruits2="orange"
# ob1=fruits()
# print(ob1.fruits1)
# print(ob1.fruits2)

class person:
    def __init__(self,name,age):
        self.name=name
        self.age= age
person=person("john",30)
print(person.name)
print(person.age)