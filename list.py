# # # # list compreansion

# # # myFruitsdata= ["apple","banana","mngo","charrry"]

# # # newList = []

# # # for item in myFruitsdata:
# # #     if "a" in item:
# # #         newList.append(item)
# # # print(newList)

# # # newlist = [x for x in range(10)]
# # # newlist = [x for x in range(10)]


# # # # sorting the list
# # # # sort ascending format
# # # list2 = ["abx",'pak','dkks']
# # # list1=[1,2,45,43,4,3,0]
# # # list2.sort()
# # # list1.sort()
# # # print(list2,list1)

# # # # sort in descending order

# # # list3=[1,2,3,333,3]
# # # list3.sort(reverse=True)
# # # print(list3)


# # # thislist = ["banana", "Orange", "Kiwi", "cherry"]
# # # thislist.sort(key = str.lower)
# # # print(thislist)

# # # Create a list of numbers from 1 to 10. Print the first element, last element, and the length of the list.

# # myList = [1,2,3,4,5,6,7,8,9,10,5]
# # print(myList[0],myList[len(myList)-1],len(myList))

# # # Append 11 and 12 to the list, then remove the number 5.

# # myList.append(11)
# # myList.append(12)
# # print(myList)
# # myList.remove(5)
# # print(myList)

# # # Replace the 3rd element of the list with 99.

# # myList.insert(3,99)
# # print(myList)

# nums = [10,20,30,40,50,60,70]
# print(nums[1:4])
# print(nums[3:])
# print(nums[:-3])
# nums.reverse()
# print(nums)

# Generate a list of squares from 1 to 10.

newList = [x**2 for x in range (11)]
print(newList)

# Generate a list of even numbers between 1 and 20.
newList2=[x for x in range(0 , 21,2)]
print(newList2)
# Given words = ["apple", "banana", "pear", "kiwi"], make a list of word lengths using comprehension.
words = ["apple", "banana", "pear", "kiwi"]

newList3=[len(x) for x in words]
print(newList3)

# From the same words, create a new list that contains only words with more than 4 letters.
newList4 = [x for x in words if len(x)>4]
print(newList4)

# Sort the list ["pear","apple","banana","kiwi"] by length (smallest → largest).
def lenList (n):
    return len(n)

newList5 = ["pear","apple","banana","kiwi","a"]
newList5.sort(key=lenList)
print(newList5)

