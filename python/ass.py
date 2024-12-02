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


a = [[1,2],[2,3],[7,9]]

a1= [[0, 0, 0], [0, 0, 0]]

for i in range (len (a)):

              for j in range (len (a[0])):

                             a1 [j][i] = a [i][j]

for r in a1:

              print (r)