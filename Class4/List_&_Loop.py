# Extracting Sublist from a List of Temperatures
# Objective: Given a list of daily temperatures for a month, extract the temperatures for a specific week (e.g., week 2).
# temperatures = [22, 24, 20, 25, 23, 26, 24, 25, 27, 29, 30, 28, 26, 27, 24, 23, 22, 21, 25, 24, 26, 27, 29, 28, 26, 25, 24, 23, 22, 21]


"""
temperatures = [22, 24, 20, 25, 23, 26, 24, 25, 27, 29, 30, 28, 26, 27, 24, 23, 22, 21, 25, 24, 26, 27, 29, 28, 26, 25, 24, 23, 22, 21]

week_in_days = 7
weeknumber = 5

start_index = (weeknumber - 1) * week_in_days
print(temperatures[start_index: start_index + week_in_days])

"""

#Extracting a Substring from a Sentence
#Objective: Given a sentence, extract and print a specific word using string slicing.
#sentence = "The quick brown fox jumps over the lazy dog"
#extract third word "brow"

"""
sentence = "The quick brown fox jumps over the lazy dog"
print(sentence[10:14])
"""

#Extracting a Sublist of Favorite Colors
#Objective: Given a list of favorite colors, extract a sublist of the first three colors using list slicing.
#favorite_colors = ["Red", "Blue", "Green", "Yellow", "Purple", "Orange"]
#extract first three colors

"""
favorite_colors = ["Red", "Blue", "Green", "Yellow", "Purple", "Orange"]
print(favorite_colors[:3])
"""



# Write a Python program to check if a list is empty or not.
# 1. output the numbers from 1 to 10 using range function and for loop
# output should be like
# 1
# 2
# 3
# etc
"""
myList = [1,2,3,4,5,6,7,8,9,10]
if len(myList) == 0 :
    print("List is Empty")
for i in range(0,len(myList)):
    print(myList[i])
    
"""

# 2. output the numbers from 35 to 50 using range function and for loop
# output should be like
# 35
# 36
# 37
# etc   
"""
for number in range(35, 51):
    print(number)

"""

# 3. output the numbers from -15 to -25 using range function and for loop
# output should be like
# -15
# -16
# -17
# etc
"""
for number in range(-15, -26, -1):
    print(number)
"""

# 4. output the numbers from 5 to -10 using range function and for loop
# output should be like
# 5
# 4
# 3
# etc

"""
for number in range(5, -11, -1):
    print(number)
"""

# 5. output the numbers from 0 to 50 incremented by 3 using range function and for loop
# output should be like
# 0
# 3
# 6
# 9
# etc
"""
for number in range(0, 51, 3):
    print(number)
"""

# 6.  Write a program to Generate Multiplication Table of 2 using range function and for loop
# output format should be like
# 2 x 1 = 2
# 2 x 2 = 4
# etc
"""
number = 2
for i in range(1, 11):
    result = number * i
    print(str(number) + " x " + str(i) + " = " + str(result))
"""

# 7. Write a Python program to sum all the items in a list use for loop. consider the list [3, 5, 2, 1, 4]
# output should be 15
# hint: 
# create a variable x outside the loop and assign the value 0
# inside the loop increment the value of x with the local variable of loop
# x += i

"""
numbers = [3, 5, 2, 1, 4]
sum_result = 0

for num in numbers:
    sum_result += num

print(sum_result)

"""

# 8. Write a Python program to get the largest number from a list and use for loop consider the list [3, 5, 2, 1, 4]
# output should be 5
# hint:
# create a variable x outside the loop and assign the value 0
# inside the loop compare the variable x with the local variable of loop
"""
numbers = [3, 5, 2, 1, 4]
max_number = numbers[0]

for num in numbers:
    if num > max_number:
        max_number = num


print(max_number)
"""

# Exercise 1: Sum of Elements in a List
# Objective: Write a Python program that calculates the sum of all elements in a given list.
# Example list
# numbers = [10, 20, 30, 40, 50]
"""

numbers = [10, 20, 30, 40, 50]
total_sum = 0
for num in numbers:
    total_sum += num

print(total_sum)

"""
# Count Even and Odd Numbers in a List
# Objective: Write a Python program that counts the number of even and odd numbers in a given list.
# Example list
# numbers = [12, 7, 9, 24, 18, 5, 3, 20]

"""
numbers = [12, 7, 9, 24, 18, 5, 3, 20]
even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even Counts : "  + str(even_count))
print("Odd Counts : "  + str(odd_count))

"""

# Print List Elements with Their Indices
# Objective: Write a Python program that prints each element of a list along with its index.
# Example list
# fruits = ["apple", "banana", "cherry", "date", "elderberry"]
# output should like
# "Index: 0 Element: apple"
# "Index: 1 Element: banana"
# "Index: 2 Element: cherry"

"""
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
index = 0
for x in fruits:
    print("Index : "+ str(index) + " Element : " + str(x))
    index = index + 1

"""

# Create a List of Even Numbers from 1 to 20
# Objective: Write a Python program that creates a list of all even numbers from 1 to 20.
"""
even_numbers = list(range(2, 21, 2))
print(even_numbers)
"""

# Find Common Elements Between Two Lists
# Objective: Write a Python program that finds and prints the common elements between two lists.
# Example lists
# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
"""
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

common_elements = []
for item in list1:
    if item in list2:
        common_elements.append(item)
print(common_elements)

"""
# Find the Length of Each String in a List
# Objective: Write a Python program that finds and prints the length of each string in a given list.
# Example list
# strings = ["apple", "banana", "cherry", "date"]

"""
strings = ["apple", "banana", "cherry", "date"]
for s in strings:
    print("Length of :" + str(s) + " : " + str(len(s)) )

"""