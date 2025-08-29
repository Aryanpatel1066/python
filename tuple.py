# Create a tuple containing 5 numbers. Print the first element and the last element.

myTupple=tuple(range(6))
print(myTupple)
print(myTupple[0],len(myTupple)-1)

t = (10, 20, 30, 40, 50, 60)
print(t[1:len(t)-1])
print(t[::-1])

# t1=(7,8)
# i=0
# while i <3:
#    print(t1)
#    i+=1

t1 = (7, 8)
t2 = t1 * 3
print(t2)


person = ("Alice", 25,"Python")
(a,b,c) = person
print(a)

t4=(10,34,55,55,5)
if 10 in t4:
      print("Yes")