# hear day 1 of learning python from basic 

#1.1 (print statement practice)

print("hello world")
print ("i am aryan patel")
print ("i am ",19,"year old")
print ("i am computerEngineering student at ldrp gandhinagar")
print(10,30,3)

#1.2 (visualize variable)

name = "aryan patel"
bloddGroup = 'B+'
fullName = '''patel arynakumar bharatkumar'''
age = 19
cgpa = 8.43
isOld = False 
isMarrid = None

print (name,bloddGroup,fullName)
print('my age is',age)
print ("cgpa from diploma is ",cgpa)
print("i am marrid ?",isMarrid)
print ("i am old?",isOld)


#1.3 (visualize the datatype)

classRoom = 'D'
labRoom = "D1" #singQuates + DoubleQuates + Triple Queates bothe are treated as string
sem = 4   
resultPanding = None 
ipass =True
sem=6 #redeclare
resultPanding = '''aai gayu'''
print(classRoom)
print(labRoom)
print(sem)
print (ipass)

print(type(sem))
print(type(ipass))
print(type(resultPanding))
print(type(labRoom))

#Q1 print sum

num1=10
num2=20
print(num1+num2)


n1 = True
n2 = False

print((20>40) or n2)

#1.4 understanding typeconversion : convert the data type from one type to another 

# two way one is typeconversion default convert by compiler automatically not by user for ex

m1=39 
m2=33.33
print(m1+m2)

# second way is type casting

m5 = int("22")
m3= 33
print(m5+m3)

# 1.5 takes input from user
#... default input type is string 

# personAge = input("Enter your age")
# print("your age is ",personAge,type(personAge))

# hear we conver the input string to whatever you want

# personMarks = int(input("Enter your age"))
# print ("your marks is",personMarks,type(personMarks))

# personSalary = float(input("Enter your salary"))
# print ("your salary is ",personSalary,type(personSalary))

# personSingle = bool(input("enter yes or no "))
# print ("you are",personSingle,type(personSalary))


"""***practice question*** """

#question1:take2 number and their sum print

# p1 = float(input("Enter the First Number :"))
# p2 = float(input("Enter the Second Number :"))

# sumOfTwo = p1+p2
# print("the sum of two number is :",sumOfTwo)

# question2: take side of squer as input from user and find the are of squre

side = float(input("Enter the value of side for Squre : "))
result = side * side  
print(result)

# question3 : two floating number from user and find average
j1 = float(input("num 1:"))
j2 = float(input("num 2:"))
avg = int((j1 + j2) / 2)
print(type(avg))

