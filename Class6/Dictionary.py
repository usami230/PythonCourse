# Create a dictionary named student_scores with the following key-value pairs:
# "Alice": 85
# "Bob": 78
# "Charlie": 92
# "Diana": 88
# "Evan": 76


student_scores = [
    {
        "name":"Alice",
        "score":85
    },
    {
        "name":"Bob",
        "score":78
    },
     {
        "name":"Charlie",
        "score":92
    },
     {
        "name":"Diana",
        "score":88
    },
     {
        "name":"Evan",
        "score":76
    },
]



# 1. Write a for loop to iterate through the student_scores dictionary and print each student's name and their score in the format: Student: [Name], Score: [Score].

"""
for item in student_scores:
    print(f"Student: {item["name"]}, Score: {item["score"]}")
"""

# 2. Write a for loop to calculate the average score of the students. Print the average score.

"""
total_score = 0
for item in student_scores:
    total_score += item["score"]
average_score = total_score / len(student_scores)

print(f"Average Score: {average_score}")
"""

# Write a for loop to assign grades based on the following criteria:
# Score >= 90: Grade A
# Score >= 80 and < 90: Grade B
# Score >= 70 and < 80: Grade C
# Score < 70: Grade D
# Store these grades in a new dictionary called student_grades.

"""
student_grades = []

for item in student_scores:
    if item["score"] >= 90:
        grade = 'A'
    elif item["score"] >= 80 and item["score"] < 90 :
        grade = 'B'
    elif item["score"] >= 70 and item["score"] < 80:
        grade = 'C'
    else:
        grade = 'D'

    student_grades.append({"name": item["name"], "grade": grade})

print(student_grades)

"""

# 4. Modify the student_scores dictionary by adding 5 bonus points to each student's score. 
# Print the updated student_scores dictionary.
"""
for item in student_scores:
    item["score"] += 5

print(student_scores)

"""


# Create a dictionary named employee_data with the following key-value pairs:
# "John": 55000
# "Emma": 60000
# "Harry": 70000
# "Sophia": 65000
# "Mike": 48000

employee_data = [
    {
        "name": "John", 
        "salary": 55000
    },
    {
        "name": "Emma", 
        "salary": 60000
    },
    {
        "name": "Harry", 
        "salary": 70000
    },
    {
        "name": "Sophia", 
        "salary": 65000
    },
    {
        "name": "Mike", 
        "salary": 48000
    },
]
# 1. Write a for loop with an if statement to identify employees who earn more than $60,000. Print their names.
"""
for item in employee_data:
    if item["salary"] > 60000:
        print(item["name"])
"""

#2. Write a for loop to increase the salary of each employee by 10%. Update the dictionary accordingly.
"""
for item in employee_data:
 
    increase_amount = item["salary"] * 0.10
    new_salary = item["salary"] + increase_amount
    item["salary"] = new_salary

print(employee_data)
"""


# Create a dictionary named library_books with the following key-value pairs:
# "The Great Gatsby": 4
# "1984": 6
# "To Kill a Mockingbird": 3
# "The Catcher in the Rye": 5
# "Moby Dick": 2

library_books = [
    {
        "book":"The Great Gatsby",
        "count" :4 
    },
    {
        "book":"1984",
        "count" :6 
    },
    {
        "book":"To Kill a Mockingbird",
        "count" :3 
    },
    {
        "book":"The Catcher in the Rye",
        "count" :5
    },
    {
        "book":"Moby Dick",
        "count" :2 
    }
]

#1. Write a for loop with range to add 2 more copies to each book. Update the dictionary accordingly.
"""
for i in range(len(library_books)):
    library_books[i]["count"] += 2
print(library_books)
"""
#2. Write a for loop to calculate the total number of books in the library. Print the total count.
"""
total_books = 0
for item in library_books:
    total_books += item["count"]

print(total_books)
"""

# Write a for loop to assign book stock categories based on the number of copies available:
# Copies >= 5: "Popular"
# Copies >= 3 and < 5: "Available"
# Copies < 3: "Limited"
# Store these stock categories in a same dict i.e library_books.

"""
for item in library_books:
    if item["count"] >= 5:
        item["stock_category"] = "Popular"
    elif item["count"] >= 3 and  item["count"] < 5: 
        item["stock_category"] = "Available"
    else:
        item["stock_category"] = "Limited"
print(library_books)
"""

# Given the dictinoary

students = {
    "Alice": {
                "Subjects": ["Math", "Science", "English"],
                "Scores": [85, 90, 78],
                "Class": 10
            },
    "Bob": {
        "Subjects": ["Math", "Science", "English"],
        "Scores": [75, 80, 88],
        "Class": 10
    },
    "Charlie": {
        "Subjects": ["Math", "Science", "English"],
        "Scores": [92, 89, 94],
        "Class": 11
    },
    "Diana": {
        "Subjects": ["Math", "Science", "English"],
        "Scores": [88, 76, 85],
        "Class": 11
    },
    "John": {
        "Subjects": ["Math", "Science", "English"],
        "Scores": [50, 60, 60],
        "Class": 11
    }
}

# 1. display Alice English Score
# 2. display Bob Class
# 3. display Charlie Math Score
"""
print(students["Alice"]["Scores"][2])
print(students["Bob"]["Class"])
print(students["Charlie"]["Scores"][0])
"""
# 4. display Diana's avg score
"""
dianascores = students["Diana"]["Scores"]
dianaavg = sum(dianascores) / len(dianascores)
print(dianaavg)
"""
# 5. display John's all subject name and score with format: Student: [Name], Score: [Subject], Score: [Score].
"""
john_subjects = students["John"]["Subjects"]
john_scores = students["John"]["Scores"]

for i in range(len(john_subjects)):
    print(f"Subject: {john_subjects[i]}, Score: {john_scores[i]}")
"""
# 6. Add new Student and its subject, score and class in same dict i.e students
"""
students["Sami"] = {
    "Subjects": ["Math", "Science", "History"],
    "Scores": [85, 90, 88],
    "Class": 10
}
print(students)
"""
# 7. add new subject and its score in John
"""
new_subject = "History"
new_score = 70

students["John"]["Subjects"].append(new_subject)
students["John"]["Scores"].append(new_score)

print(students)
"""


students = [
    {
        "name": "Alice",
        "subjects": ["Math", "Science", "English"],
        "scores": [85, 90, 78],
        "Class": 10
    },
    {
        "name": "Bob",
        "subjects": ["Math", "Science", "English"],
        "scores": [75, 80, 88],
        "Class": 10
    },
    {
        "name": "Charlie",
        "subjects": ["Math", "Science", "English"],
        "scores": [92, 89, 94],
        "Class": 11
    },
    {
        "name": "Diana",
        "subjects": ["Math", "Science", "English"],
        "scores": [88, 76, 85],
        "Class": 11
    }
]

#1. display Alice English Score
"""
for item in students:
   if item["name"] == "Alice":
      for sub in range(len(item["subjects"])) :
            if item["subjects"][sub] == "English":
               print( item["scores"][sub])
               break
"""

# 2. display Bob Class
"""
for item in students:
   if item["name"] == "Bob":
      print(item["Class"])
"""

# 3. display Charlie Math Score

# for item in students:
#    if item["name"] == "Charlie":
#       for sub in range(len(item["subjects"])) :
#             if item["subjects"][sub] == "Math":
#                print( item["scores"][sub])
#                break

# 4. display Diana's avg score
"""
diana_avg_score = None
total_score = 0
count = 0
for item in students:
    if item["name"] == "Diana":
        count = len(item["scores"])
        for sub in range(len(item["subjects"])) :
            total_score += item["scores"][sub]
     
      
diana_avg_score = total_score / count
print(diana_avg_score)
"""
#5. display John's all subject name and score with format: Student: [Name], Score: [Subject], Score: [Score].
"""
for item in students:
   if item["name"] == "Charlie":
      for sub in range(len(item["subjects"])) :
           print(f"Student: {item["name"]}, subject: {item["subjects"][sub]}, Score: {item["scores"][sub]}")
"""
#6. display which class obtained the higher marks
"""
class_total_scores = {}
for item in students:
    class_name = item["Class"]
    total_score = sum(item["scores"])
  
    if class_name in class_total_scores:
        class_total_scores[class_name] += total_score
    else:
        class_total_scores[class_name] = total_score


highest_class = None
highest_total_score = 0

for class_name in class_total_scores:
    if class_total_scores[class_name] > highest_total_score:
        highest_total_score = class_total_scores[class_name]
        highest_class = class_name

print(f" {highest_class}")
"""

# 7. display the student name that obtain high marks in subject Math in class 10

"""
highest_math_score = 0
top_math_student = None


for item in students:
    if item["Class"] == 10:
        math_index = item["subjects"].index("Math")
        math_score = item["scores"][math_index]
        
        if math_score > highest_math_score:
            highest_math_score = math_score
            top_math_student = item["name"]

print(top_math_student)

"""

# 8. Add new Student and its subject, score and class in same dict i.e students
"""
new_student = {
    "name": "Sami",
    "subjects": ["Math", "Science", "English"],
    "scores": [80, 85, 90],
    "Class": 10
}
students.append(new_student)

print(students)
"""