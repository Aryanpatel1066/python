# # class Parent:
# #     def greet(self):
# #         print("hello i am from parent class")
# # class Chaild(Parent):
# #     def greet(self):
# #         super().greet()#call parent first after i execute
# #         print("hello i am from child class")

# # chaildObj = Chaild()
# # chaildObj.greet()


# class H1():
#      def __init__(self,msg):
#           self.msg = msg
#           print("from parent"+msg)
# class H2(H1):
#      def __init__(self,msg):
#           super().__init__(msg)
#           self.msg=msg
#           print("from chaild"+msg)
# h2Obj = H2("Radhe Radhe")


# super keyword

# class Hello:
#     msg = "hello"

#     @classmethod
#     def sayHelllo(cls,msg):
#         # cls.msg=msg
#          Hello.msg=msg
# obj = Hello()
# obj.sayHelllo("good")
# print(obj.msg)
# print(Hello.msg)

print([1,2,3]+[1,2,3])