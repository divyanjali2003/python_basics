list1=["red","rose","black","white","blue"]

# list1.insert(2,"brown")
# print(list1)

# for x in list1:
#     print(x)

# list2=[4,5,6]
# list1.extend(list2)
# print(list1)

# print(list1[3])

# print(list1[0])

# print(list1[1])

# print(list1[2])

# print(list1[4])

# print(list1[-2:-1])

# list1[4]="brown"
# print(list1)

# n=int(input("Enter a number"))
# factorial=1
# for i in range(1,n+1):
#     factorial=factorial*i
# print("Factorial of the given number is",factorial)

# list1=[1,2,3,4,5,6]
# list2=sum(list1)
# print(list2)

# list2=("apple","banana","orange")
# list4=sum(list2)
# print(list4)

# numbers=(2,3,4,5,6,7)
# sum=sum(numbers)
# print(sum)

# dic1={1,2,3,4,5,6,7,8,9}
# dic2=sum(dic1)
# print(dic2)

# a1= [[1, 1, 1, 1], 
#      [2, 2, 2, 2], 
#      [3, 3, 3, 3], 
#      [4, 4, 4, 4]]
# result=[[row[i] for row in a1] for i in range(len(a1[0]))]
# for row in result:
#     print("join([str(element) for element in row])")     


# a = [[1,2],[2,3],[7,9]]
# a1= [[0, 0, 0], [0, 0, 0]]
# for i in range (len (a)):
#     for j in range (len (a[0])):
#         a1 [j][i] = a [i][j]
# for r in a1:
#   print (r)

# class string1:
#     def __init__(self,str1):
#         self.str1=str1
#     def input_str3(self):
#         self.str1=input("enter a string:")
#     def output_str4(self):
#         print ("string is:")
#         print(self.str1)
# a=string1()
# a.input_str3()
# a.output_str4()

# class String1:
#     def __init__(self, str1=""):
#         self.str1 = str1
#     def input_string(self):
#         self.str1 = input("Enter a string:")
#     def output_string(self):
#         print("String is:")
#         print(self.str1)
# a = String1()
# a.input_string()
# a.output_string()

# class company:
#     def __init__(self,name, salary):
#         self.name=name
#         self.salary=salary
#     def employe(self):
#         print(self.name,self.salary)
# x=company("Divya",2000000)
# x.employe()

# class circle:
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         return self.radius**2*3
#     def distance(self):
#         return self.radius*2*3
# circle1=circle(4)
# print(circle1.area())
# print(circle1.distance)

class BankAccount:
    def __init__(self,account_number,balance):
        self.__account_number=account_number
        self.__balance=balance
    def _display_balance(self):
        print("balance:",self.__balance)
b=BankAccount(1234567890,5000)
b._display_balance()

class Shape:
    def __init__(self):
        self.area_value=0
    def area(self):
        print(f"Area of the shape:")
class Square(Shape):
    def __init__(self, length):
        super().__init__() 
        self.length = length
        self.area_value = self.length**2
    def area(self):
        print(f"Area of the square:")
shape = Shape()
shape.area()
square = Square(5)
square.area()