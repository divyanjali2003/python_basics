# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print("Name:",self.name)
#         print("Age:",self.age)
# s=student("jhon",20)
# s.display()

# class company:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print("Name:",self.name)
#         print("Age:",self.age)
# s=company("Divya Dileep",21)
# s.display()

# class BankAccount:
#     def __init__(self,account_number,balance):
#         self.__account_number,balance
#         self.__balance=balance
#     def _display_balance(self):
#         print("balance:",self.__balance)
# b=BankAccount(1234567890,5000)
# b.__display_balance()

# class company:
#     def __init(self,employes,tranies):
#         self.__employes,tranies
#         self.__tranies=tranies
#     def _display_tranies(self):
#         print("tranies:",self.__tranies)
# b=company(300,3)
# b.__display_tranies()

class person:
    def __init__(self,name,age):
        self._name=name
        self._age=age
    def _display(self):
        print("Name:",self._name)
        print("Age:",self._age)
class student(person):
    def __init__(self,name,age,roll_number):
        super().__init__(name,age)
        self._roll_number=roll_number
    def display(self):
        self._display()
        print("Roll.Number:",self._roll_number)
s=student("divya",20,123)
s.display()
