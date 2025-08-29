# s1 = {1,2,3,4,21,1,2}
# print(s1)

# thisset = {"apple", "banana", "cherry"}

# print("banana" in thisset)


# thisset = {"apple", "banana", "cherry"}
# mylist = ["kiwi", "orange"]

# thisset.update(mylist)

# print(thisset)

# thisset = {"apple", "banana", "cherry"}

# thisset.remove("banana")

# print(thisset)


s2 = set((range(1,6)))
s2.add(6)
s2.remove(3)
print(4 in s2)
print(s2)


fruitSet = set()   # correct empty set
list1 = ['apple', 'banana']

fruitSet.update(list1)  # add all elements from list
print(fruitSet)


A = {1, 2, 3, 4}  
B = {3, 4, 5, 6}
print(A.union(B))
print(B.union(A))
print(A.difference(B))
print(A-B)
print(B-A)
print(A.symmetric_difference(B))