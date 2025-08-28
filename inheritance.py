class A:
    def lastName(self):
        print("patel")
class B:
    def firstName(self):
        print("aryan")
class C(A,B):
    def middleName(self):
        print("abc")
cObj = C()
cObj.firstName()
cObj.lastName()
cObj.middleName()