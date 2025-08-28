# # for x in "banana":
# #  print(x)
# # my_list = [1,2,"hello"]
# # print(my_list[2])
# # r = list(range(5))
# # print(r)
# # fruits = ["apple","banana","xyz"]
# # firstFruit =fruits[0]="graps"
# # print(fruits)
# # print(firstFruit)

# # x = "hello"
# # y = 5
# # print(7+9)

# # squres = []

# # for x in range(5):
# #     squres.append(x**2)
# # print(squres)

# # unpac the tupple 

# fruits = ("apple","banana","cheryry")
# (a,b,c)=fruits
# print(a,b,c)

# num = {1,2,3,4,1}
# print(num)

# fruits2 = {"apple", "banana", "cherry"}

# print(fruits2)  
# # Output could be: {'banana', 'cherry', 'apple'}
# # Or: {'cherry', 'apple', 'banana'}

class Car:
    def __init__(self,location):
        self.location=location
        print("consturctor called")
 
    name="bmw"
    color="red"
   

carObj = Car("india")
print(carObj.name)
print(carObj.color)
print(carObj.location)