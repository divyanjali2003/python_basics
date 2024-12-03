# x=56
# def my_func():
#     print("value of x is",x)
# my_func()    

def my_function(fname,age):
  print(fname + " Gomez")
  print("age is",age)

my_function("jiji",24)



def add_numbers( a = 7,  b = 8):
    sum = a + b
    print('Sum:', sum)


# # function call with two arguments
# add_numbers(2, 3)

# # #  function call with one argument
# # add_numbers(a = 2)

# # function call with no arguments
# add_numbers()


# def display_info(first_name, last_name,age):
#     print('First Name:', first_name)
#     print('Last Name:', last_name)
#     print('Last Name:', age)

# display_info(last_name = 'Cartman', first_name = 'Eric',age=25)



def find_sum(*numbers):
    result = 0
    
    for num in numbers:
        result = result + num
    
    print("Sum = ", result)

# function call with 3 arguments
find_sum(1, 2, 3,7,8)

# # function call with 2 arguments
# find_sum(4, 9)