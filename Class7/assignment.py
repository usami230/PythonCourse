# loop
# Write a program to display index and the values (both) of a list using for loop. consider a list l = [100, 200, 300, 400]
# output: 
# 0 100
# 1 200
# 2 300
# 3 400

"""
arry = [100, 200, 300, 400]
for index, value in enumerate(arry):
    print(index, value)
"""


# Write a program that find common values between 2 lists and also tells how many times the common value occurs.
# consider the list l1 = ['a', 'b', 'c', 'd'] and l2 = ['e', 'b', 'g', 'd', 'f', 'h']
# output:
# {"a": 1, "b": 2, "c": 1, "d": 2, "e": 1, "f": 1, "g": 1, "h": 1}
# hint: use nested loop

"""
arry1 = ['a', 'b', 'c', 'd']
arry2 = ['e', 'b', 'g', 'd', 'f', 'h']

common_counts = {}
combined_list = arry1 + arry2
for item in combined_list:
    count = 0
    for sublist in [arry1, arry2]:
        count += sublist.count(item)
    common_counts[item] = count

print(common_counts)
"""

# consider the number 2783, the number consists of 4 digits.
# Count the total number of digits in a number using while loop.
# instruction (hint):
# x = 2783
# counter = 0
# run while loop as long as x becomes 0
# increment the counter inside while loop
# divide x by 10 using floor division syntax "//"

"""
x = 2783
counter = 0
print( 10 // 3)
while x > 0:
    x = x // 10  

    counter += 1  

print("Total number of digits:", counter)

"""



# Write a program that takes user input and display it. The program keep ask user the input until user enters “0”
"""
while True:
    user_input = input("Enter something (enter '0' to stop): ")
    if user_input == "0":
        break
    print("You entered:", user_input)
"""
# Write a program and ask user to enter number, 5 times using while loop. store each value in list.
# calculate the sum of all values in a list


"""
numbers = []
counter = 0
while counter < 5:
    user_input = int(input("Enter a number: "))
    numbers.append(user_input)  
    counter += 1  

total_sum = sum(numbers)

print("Numbers entered:", numbers)
print("Sum of all numbers:", total_sum)

"""


# Write a program to ask for a name until the user enters END. Print the name each time. When you are done, print "I am done."
"""
while True:
    name = input("Enter a name (type 'END' to stop): ")
    if name.lower() == "END":
        print("I am done.")
        break
    print("You entered:", name)
"""
# consider the list l1 [11, 33, 50]. use for loop to output the result like "113350"

"""
arry = [11, 33, 50]

result = ""
for number in arry:
    result += str(number)

print(result)

"""

# consider the following list ['cat', 'dog', 'hand', 'freedom', 'jump', 'frog', 'happy', 'popcorn', 'tiger']
# display the word that contains character longer than 5
# the output should be freedeom and popcorn

"""
arry = ['cat', 'dog', 'hand', 'freedom', 'jump', 'frog', 'happy', 'popcorn', 'tiger']
for word in arry:
    if len(word) > 5:
        print(word)
"""

# Write a program to create a function that takes two arguments, name and age. print them inside function.
"""
def name_and_age(name, age):
    print("Name:", name)
    print("Age:", age)


name_and_age("Sami", 28)

"""




# Write a program to create a function show_employee() using the following conditions.
# It should accept the employee’s name and salary and display both.
# If the salary is missing in the function call then assign default value 9000 to salary
"""
def show_employee(name, salary=9000):
    print("Employee Name:", name)
    print("Employee Salary:", salary)


show_employee("sami", 12000)  
show_employee("fahad")

"""


# Write function that accepts different values as parameters and returns a list
# consider the below varables
# a = 4
# b = 8
# c = 10
# d = 12
# pass above values to the function and return the list
# output: [4, 8, 10, 12]


"""

def create_list(*args):
    return list(args)
a = 4
b = 8
c = 10
d = 12

result_list = create_list(a, b, c, d)
print(result_list)

"""


# Write a function called km_to_miles that takes kilometers as a parameter, converts it into miles and returns the result.
"""
def km_to_miles(km):
    miles = km * 0.621371  
    return miles

kilometers = 10
miles = km_to_miles(kilometers)
print(f"{kilometers} kilometers is equal to {miles} miles.")
"""


# Write a function called is_divisable_by_11 that takes an integer as an parameter and returns whether it is divisible by 11 or not.
"""
def is_divisible_by_11(number):
    if number % 11 == 0:
        return True
    else:
        return False

num1 = 22
num2 = 25

print(f"{num1} is divisible by 11: {is_divisible_by_11(num1)}")
print(f"{num2} is divisible by 11: {is_divisible_by_11(num2)}")
"""

# Write a function called get_highest that takes 2 numbers as parameters and returns the highest of the 2 numbers.
"""
def get_highest(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


a = 15
b = 28
highest_number = get_highest(a, b)
print(f"The highest number between {a} and {b} is: {highest_number}")

"""