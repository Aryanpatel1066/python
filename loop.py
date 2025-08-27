# 1 Print numbers from 1 to 10 using a for loop.

# for i in range (11,0,-2):
#   print(i)

#2  Print the multiplication table of 5 (from 5 x 1 up to 5 x 10).

# for i in range (1,11):
#   print(i*5)

#3 Print all even numbers between 1 and 50.

# for i in range (1,51,2):
#     print(i)

#4 Print the sum of numbers from 1 to 100.

# sum =0
# for i in range(1,101):
#     sum = sum + i
# print(sum)

# Count how many vowels (a, e, i, o, u) are in a given string.

# vowels = {'a','e','i','o','u'}
# string = "apple"
# count =0
# for i in string:
#     for j in vowels:
#         if i == j:
#             count+=1
# print(count)

# vowels = {'a', 'e', 'i', 'o', 'u'}
# string = "Apple"
# count = 0

# for i in string.lower():   # convert whole string to lowercase
#     if i in vowels:
#         count += 1

# print("Number of vowels:", count)

# *
# **
# ***
# ****
# *****

for i in range(1, 6):
    for j in range(1, 6):
        if i >= j:
            print("*", end="")    
        # else:
        #     print("_", end="")   
    print()  