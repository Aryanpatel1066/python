class Student:
    # define constructor
    def __init__(self, marks):
        self.__marks = marks #private variable

# read 
    @property
    def marks(self):    
        return self.__marks
# setter
    @marks.setter
    def marks(self, value):   # setter
        if value < 0:
            print("❌ Marks cannot be negative")
        else:
            self.__marks = value
s = Student(90)
print(s.marks)    # getter looks like attribute

s.marks = 95      # setter looks like assignment
print(s.marks)

s.marks = -20     # ❌ rejected by setter

