# tuple1=("apple","banana","cherry")
# print(tuple1)

# tuple1=("divya","drishya","susan","dileep")
# print(tuple1)/

# tuple2=("apple","banana","cherry")
# print(len(tuple2))

# tuple2=(2,3,4,65,8)
# print(len(tuple2))

# tuple1=("apple","banana","cherry")
# tuple2=(1,2,3,4,5)
# tuple3=("true","false","true")
# print(tuple1)
# print(tuple2)
# print(tuple3)

# tuple1=("divya","drishya")
# tuple2=(26,21)
# tuple3=(1,2,3,4,5)
# print(tuple1)
# print(tuple2)
# print(tuple3)

# tuple4=("apple","banana","cherry")
# print(type(tuple4))

# tuple4=(21,34,56)
# print(type(tuple4))

# tuple5=("apple","banana","cherry")
# print(tuple5[2])

# tuple5=("divya","drishya")
# print(tuple5[0])

# tuple6=("apple","chery","banana")
# print(tuple6[-2])

# tuple6=(2,3,4,5,67)
# print(tuple6[-3])

# tuple7=("apple","orange","banana","chery","kiwi","lemon")
# print(tuple7[3:5])/

# tuple7=(2,3,4,5,6,7,8,9)
# print(tuple7[2:4])

# tuple8=("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(tuple8[:4]

# tuple8=(1,2,3,4,5,6,7,8,9,10)
# print(tuple8[:5])

# tuple9=("apple","banana","kiwi","chery","orange")
#print(tuple[-3:-1])

# tuple9=(2,4,6,8,10,12)
# print(tuple9[-5:-1])

# x=("apple","banana","chery")
# y=list(x)
# y[2]="kiwi"
# x=tuple(y)
# print(x)

# x=(1,2,3,4,5,6,7,8,9)
# y=list(x)
# y[3]=10
# x=tuple(y)
# print(x)

# tuple10=("apple","banana","chery","orange")
# y=list(tuple10)
# y.append("lemon")
# tuple10=tuple(y)
# print(tuple10)

# tuple10=(1,2,3,4,5,6,7,8,9)
# y=list(tuple10)
# y.append(10)
# tuple10=tuple(y)
# print(tuple10)/

# tuple12=(2,3,4,5,6,7,8)
# for x in tuple12:
#     print(x)

# tuple13=(2,3,4,5,6,7)
# for x in range(len(tuple13)):
#     print(x)

# tuple14=("apple","banana","cherry")
# i=0
# while i<len(tuple14):
#   print(tuple14[i])
# i=i+1

# tuple12=("divya","drishya")
# tuple13=(21,26)
# tuple14=tuple12+tuple13
# print(tuple14)

# set2={"apple","banana","chery"}
# print(set2)

# set3={"apple","banana","chery","true",12,16}
# print(set3)

# set4={"apple","banana","cherry",29,"true",45,"false"}
# print(len(set4))

# set5={"divya","drishya"}
# set6={2,3,4,4}
# set7={"true","true","true"}
# print(set5)
# print(set6)
# print(set7)

# set1={}"apple","banana","chery"}
#print(type(set1))

# set2={"divya","drishya"}
# for x in set2:
#     print(x)

# set3={"divya","drishya"}
# print("kavya" in set3)

# set4={2,3,4,5,5,6,6,77}
# set4.add(100)
# print(set4)

# set5={"apple","banana"}
# list3=["orange","kiwi"]
# set5.update(list3)
# print(set5)

# set6={"divya","drishya"}
# set6.remove("divya")
# print(set6)

# set6={"divya","drishya"}
# set6.discard("divya")
# print(set6)

# set6={"divya","drishya"}
# x=set6.pop()
# print(x)

# set6={"divya","drishya"}
# set6.clear()
# print(set6)

# set6={"divya","drishya"}
# for x in set6:
#     print(x)

# set6={"divya","drishya"}
# set4={1,2,3,4,5}
# set3=set6.union(set4)
# print(set3)


# list1=[2,4,6,8]
# sqr=list(map(lambda x:x**3,list1))
# print(sqr)

# list1=[1,2,3,4,7,12,34,56]
# even=list(filter(lambda x:x%2==0,list1))
# print(even)


list1=[1,2,3,4,7,12,34,56]
from functools import reduce
productt=reduce(lambda x,y:x*y,list1)
print(productt)

