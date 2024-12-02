# list1=[2,4,6,5]
# sqr=list(map(lambda x:x**2,list1))
# print(sqr)

# list3=[3,4,5,5,7,7,55]
# sqr=list(map(lambda x:x**3,list3))
# print(sqr)

# list2=[2,3,4,4,5,6,7]
# even=list(filter(lambda x:x%2==0,list2))
# print(even)

# list3=[5,2,15,72,35,82]
# odd=list(filter(lambda x:x%2==0,list3))
# print(odd)

# list5=[3,4,5,6,7,8,6]
# from functools import reduce
# product=reduce(lambda x,y:x*y,list5)
# print(product)

list4=[2,3,4,5,7,8,9,23]
from functools import reduce
product=reduce(lambda x,y:x*y,list4)
print(product)
