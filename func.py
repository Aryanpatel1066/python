# def add(a,b):
#     return a+b
# print(add(b=10,a=3))

# #one kind of the desturucturing 
# fruits = ["apple", "banana", "cherry"]
# x, y, z = fruits
# print(x)
# print(y)
# print(z)

# listOfNum = (3,"hello")
# print(listOfNum[1])


# def hello():
#   return "hello"
# print(hello)

# average of 3 numbers

# def avgOf3(a,b,c):
#   sum = a+b+c
#   avg = sum/3
#   return avg

# output = avgOf3(10,20,0)
# print(output)

# print("hello", end=" ")
# print("yyy")

# def sum(a=2,):
#     return a
# print(sum())

# write a program for length of list

# def lengthOfList(list):
#     return len(list)

# myList = [1,2,"hello"]
# result = lengthOfList(myList)
# print(result)

# print list in single line

# def takeAList(list):
#     for i in list:
#         print(i, end=" ")

# takeAList(["hello",1,2,3])

# find the factorial

# def factorial(n):
#     result =1
#     for i in range(1,n+1):
#         result = result*i
#     return result

# print(factorial(5))

# print for odd even

# def isOddOrEven(num):
#     if (num % 2 ==0):
#         return "even"
#     else:
#         return "odd"
# print(isOddOrEven(5))
      


# recursion

# def myrecur(n):
#     if(n==0):
#         return
#     print(n)
#     myrecur(n-1)
# myrecur(5)

# write a function for n sum use recursion

def nSum(num):
    if(num ==0 or num ==1):
        return num
    return num+nSum(num-1)

print(nSum(10))
    