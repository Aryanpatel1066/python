# # create student class hat takes name and marks of 3 subjects as arguments as
# # argument in constructor .then create a method to print average

# class Studens:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
         
         
#     def avgOfStudent(self):
#         sum = 0
#         for val in self.marks:
#             sum = sum+val
#         print(f"hii{self.name} your average marks is {sum/3}")
# # person 1
# studentObj = Studens("aryan",[10,20,0])
# studentObj.avgOfStudent()
# # person2
# studentObj.name="assf"
# studentObj.avgOfStudent()
# # print(ans)

# static method 

class JustHello:
    def sayHello1(self):
        print("hey whatsApp")

    @staticmethod #decorator
    def sayHello2():
        print("hey whatsApp")
    
obj1 = JustHello()
obj1.sayHello1()
obj1.sayHello2()