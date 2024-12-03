# def my_function(fname, age):
#     print(fname + " gomez")
#     print("age is",age)
# my_function("jiji",24)

# def add_number(a=7,b=8):
#     sum=a+b
#     print('sum:', sum)
# # add_number(2,3)
# # add_number(a=2)
# add_number()

# def display_info(first_name, last_name,age):
#     print('First Name:', first_name)
#     print('Last Name:', last_name)
#     print('Last Name:', age)
# display_info(last_name = 'Dileep', first_name = 'Divya',age=21)

# def find_sum(*numbers):
#     result = 0
#     for num in numbers:
#         result = result + num
#     print("Sum = ", result)
# find_sum(1,2,3,4,5)
# find_sum(4,9)

# def my_function():
#     yield 1
#     yield 2
#     yield 3
# for value in my_function():
#         print(value)

# def my_function():
#     yield 2
#     yield 4
#     yield 6
# x= my_function()
# print(next(x))
# print(next(x))
# print(next(x))

sqr_generator=(i*i for i in range(10))
for i in sqr_generator:
    print(i)





