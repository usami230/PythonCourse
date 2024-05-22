# take 2 input from the user
# write your name
# write your age
# display its value and type side by side

# solution
name = input("write your name: ")
age = input("write your age: ")

print(name, type(name))
print(age, type(age))



# ask user 2 numbers and display a their sum;

# sotution
num_1 = input("enter a number")
num_2 = input("enter another number")

num_1 = int(num_1)
num_2 = int(num_2)

result = num_1 + num_2
print(result)


# write a program to ask user his name and display the message
# Hi, {name}, Welcome back

# solution
name = input("write your name")
message = "Hi " +name+ "! "+ "Welcome back"
print(message)



# Accept 2 numbers from the user and display its sum, multiplication and divison

num_1 = int(input("write numer"))
num_2 = int(input("write another num"))


sum = num_1 + num_2
print(sum)

multiplication = num_1 * num_2
print(multiplication)

div = num_1 // num_2
print(div)


# input function discussion
# print("hell world")

# demonstrating line by line execution demo
# print("hellow world 1")
# input("write you name")
# print("hellow world 2")

# store user input in variable
name = input("write your name")
print(name)

# store user input in variable and convert it to integer
age = input("write your age")
age = int(age)
print(age)