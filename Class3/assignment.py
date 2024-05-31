# Q1 Write a program to check whether a person is eligible to vote or not?


"""
age = int(input("Enter Age :"))
if age >= 18 :
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")
"""

# Q2 Write a program to check char is vowel or not.

"""
char = input("Enter Alphabet : ")
if(char.lower() == "a" or 
   char.lower() == "e" or 
   char.lower() == "i" or 
   char.lower() == "o" or 
   char.lower() == "u"):

    print("The character is a vowel")
else :
    print("The character is not a vowel")
"""

# Q3 Write a program to check the number is positive or negative. User input.

"""
number = int(input("Enter Number : "))
if number < 0:
    print("Negtive")
else :
   print("Positive")  
"""

# Q4 Write a program to check whether a number is odd or even?

"""
number = int(input("Enter Number : "))
if number % 2 == 0 :
    print("Even")
else :
    print("Odd")

"""

 # Q5 Write a program to display the grade of the user in subject A, ask user marks obtained out of 100

""" 
number = int(input("Enter Number : "))
 
if number >= 80:
    print('A+')
elif number >= 70:
    print('A')
elif number >= 60:
    print('B')
elif number >= 50:
    print('D')     
else:
    print('Fail')   

""" 

#Q6 Write a program to check whether a number is divisible by 7
"""
number = int(input("Enter Number : "))
if number % 7 == 0 :
    print("Divisible by 7")
else :
    print("Not divisible by 7")
"""

#Q7 Write a program to check if year is leap year.
"""
year = int(input("Enter Year : "))

if (year % 4 == 0):
    print("Leap Year") 
else :
     print("Not Leap Year") 
"""
#Q8 Write a program to ask user its name and check whether name consists of 5 or more letters
"""
name = input("Enter Name : ")
if len(name) == 5 :
    print("name consists of 5 letters")
elif len(name) >= 5 :
    print("letters are more then 5")
else :
    print("letters are less then 5")
"""

# Q9 Write a program that accepts 3 inputs from user. input 1 and input 2 should be numbers and the third input should be mathematical operator.
"""
value_one = int(input("Enter one value : "))
value_two = int(input("Enter two value : "))
operator = input("Enter Opertor : ")
if operator == "+" :
    print("Add : " + str(value_one + value_two))
elif operator == "-" :
    print("Sub : " + str(value_one - value_two))
elif operator == "*" :
    print("Mul : " + str(value_one * value_two))
else :
    print("Mul : " + str(value_one / value_two))
"""


# Q10  Write a program that accepts 1 input from user and check if the number is divisible by 2 and 3 both.
"""
value_one = int(input("Enter one value : "))
if  value_one % 2 == 0 and value_one % 3 == 0 :
    print("divisible by 2 or 3")
elif value_one % 2 == 0 :
    print("divisible by 2")
elif value_one % 3 == 0 :
    print("divisible by 3")
else : 
    print("Not divisible by 2 or 3")
"""

# Q11 Write a program that accepts 2 inputs from user and check which number is largest.

"""
value_one = int(input("Enter one value : "))
value_two = int(input("Enter two value : "))

if value_one > value_two:
    print(str(value_one) + " is largest " + str(value_two) )
elif value_two > value_one :
    print(str(value_two) + " is largest " + str(value_one))
else:
    print("Both numbers are equal")
"""

# Q12 Write a program that accepts 3 input from user and check which number is largest.

"""
value_one = int(input("Enter one value : "))
value_two = int(input("Enter two value : "))
value_three = int(input("Enter three value : "))

if value_one >= value_two and value_one >= value_three :
    print(str(value_one) + " is largest " + str(value_two) + " or "+ str(value_three))
elif value_two >= value_one and value_two >= value_three:
     print(str(value_two) + " is largest " + str(value_one) + " or "+ str(value_three))
else : 
     print(str(value_three) + " is largest " + str(value_one) + " or "+ str(value_two))

"""
#Q13 Write a program that accepts 3 input from user and check the second largest.

"""
value_one = int(input("Enter one value : "))
value_two = int(input("Enter two value : "))
value_three = int(input("Enter three value : "))

if (value_one >= value_two and value_one <= value_three) or (value_one <= value_two and value_one >= value_three):
    print("Second Highest : " + str(value_one))
elif (value_two >= value_one and value_two <= value_three) or (value_two <= value_one and value_two >= value_three):
    print("Second Highest : " + str(value_two))
else:
    print("Second Highest : " + str(value_three))
"""

#Q14 Write a python program that accept user an input. The valid input should be of following
"""
color = input("Enter the color of the signal: ")  
if color.lower() == "green":
    print("Car is allowed to go")
elif color.lower() == "red":
    print("Car has to stop")
elif color.lower() == "yellow":
    print("Car has to wait")
else:
    print("Invalid input")
"""

#Q15 Write a program that takes a password as input and checks its strength:
"""
password = input("Enter your password: ")
if len(password) < 6:
    print("Weak password")
elif len(password) >= 6 and len(password) <= 12:
    print("Moderate password")
else:
    print("Strong password")
"""

#Q16 Write a program that takes an employee's salary and years of service as input. Calculate the bonus as follows:
"""
salary = int(input("Enter the employee salary: "))
years = int(input("Enter the employees years of service: "))


if years < 5:
    bonus = 0
elif years >= 5 and years <= 10:
    bonus = 0.1 * salary
else:
    bonus = 0.2 * salary
print("The bonus amount for the employee is : " + str(bonus))
"""


#Q17 Write a program that takes the total amount of a purchase as input and applies a discount:
"""
total_amount = int(input("Enter the total amount :"))

if total_amount < 100:
    discount = 0
elif total_amount >= 100 and total_amount <= 500:
    discount = 0.1 * total_amount
else:
    discount = 0.2 * total_amount

final_amount = total_amount - discount

print("The final amount after discount is: " + str(final_amount))
"""

#Q18 Write a program that takes a person's age as input and prints the age group they belong to:
"""
age = int(input("Enter age: "))
if age < 13:
    print("Child")
elif age >= 13 and age <= 19:
    print("Teenager")
else:
    if age < 65:
        print("Adult")
    else:
        print("Senior")
        
"""

#Q19 Write a program that checks if a customer is eligible for a discount based on their membership status and purchase amount:
"""
ismember = input("Are you a member? (yes/no): ").lower()
purchase_amount = int(input("Enter the purchase amount: "))

if ismember == "yes":
    if purchase_amount >= 50:
        print("Eligible for 10% discount")
    else:
        print("Eligible for 5% discount")
else:
    if purchase_amount >= 100:
        print("Eligible for 5% discount")
    else:
        print("No discount")
"""


card_type = input("Enter card type (affiliated_card/govt_employee): ")
age = int(input("Enter your age: "))
amount = int(input("Enter amount to withdraw: "))
grade = int(input("Enter your grade (if applicable, else enter 0): "))

   
if card_type == "govt_employee":
    
    if grade < 18:
            amount += 10
    print("Amount withdrawn: Rs. "+str(amount))
elif card_type == "affiliated_card" and age < 60:   
    if grade < 18:
            amount += 10
    print("Amount withdrawn: Rs.  "+str(amount))
else:
    print("Sorry, you are not eligible to withdraw money.")