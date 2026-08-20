files = {
    "set1.py": '''s = {10, 20, 30, 40, 50}
for i in s:
    print(i)
''',

    "set2.py": '''a = [10, 20, 10, 30, 20, 40]
s = set(a)
print(s)
''',

    "set3.py": '''fruits = {"Apple", "Banana", "Mango", "Orange", "Grapes"}
fruits.add("Pineapple")
fruits.add("Watermelon")
print(fruits)
''',

    "set4.py": '''s = {10, 20, 30, 40, 50}
s.remove(30)
print(s)
''',

    "set5.py": '''students = {"Amit", "Rahul", "Sneha", "Priya", "Rohan"}
name = input("Enter student name: ")

if name in students:
    print("Student exists")
else:
    print("Student does not exist")
''',

    "set6.py": '''cities = {"Pune", "Mumbai", "Kolhapur", "Nashik", "Nagpur"}
print("Total cities =", len(cities))
''',

    "set7.py": '''lang = {"Python", "Java", "C++", "JavaScript", "Dart"}

for i in lang:
    print(i)
''',

    "set8.py": '''a = [10, 20, 10, 30, 40, 20, 50, 30]
s = set(a)
print(s)
''',

    "set9.py": '''a = {1, 2, 3, 4}
b = {4, 5, 6, 7}
print(a | b)
''',

    "set10.py": '''a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print(a & b)
''',

    "set11.py": '''a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print("First only:", a - b)
print("Second only:", b - a)
''',

    "set12.py": '''a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print(a ^ b)
''',

    "set13.py": '''a = {1, 2, 3}
b = {1, 2, 3, 4, 5}

if a.issubset(b):
    print("First set is subset")
else:
    print("First set is not subset")
''',

    "set14.py": '''a = {1, 2, 3, 4, 5}
b = {1, 2, 3}

if a.issuperset(b):
    print("First set is superset")
else:
    print("First set is not superset")
''',

    "set15.py": '''a = {1, 2, 3}
b = {4, 5, 6}

if a.isdisjoint(b):
    print("No common elements")
else:
    print("Common elements are present")
''',

    "set16.py": '''a = {1, 2, 3, 4}
b = {4, 3, 2, 1}

if a == b:
    print("Sets are equal")
else:
    print("Sets are not equal")
''',

    "set17.py": '''student1 = {"Python", "Java", "DBMS", "OS"}
student2 = {"Java", "DBMS", "CN", "AI"}

print("Common subjects:", student1 & student2)
''',

    "set18.py": '''a = input("Enter a sentence: ")
words = set(a.split())

for i in words:
    print(i)
''',

    "set19.py": '''morning = {"Amit", "Rahul", "Sneha", "Priya", "Rohan"}
afternoon = {"Sneha", "Priya", "Kiran", "Neha", "Rohan"}

print("Both:", morning & afternoon)
print("Morning only:", morning - afternoon)
print("Afternoon only:", afternoon - morning)
print("At least one:", morning | afternoon)
''',

    "set20.py": '''python = {"Amit", "Rahul", "Sneha", "Priya", "Kiran"}
java = {"Sneha", "Priya", "Rohan", "Neha", "Kiran"}

print("Python:", python)
print("Java:", java)
''',

    "set21.py": '''python = {"Amit", "Rahul", "Sneha", "Priya", "Kiran"}
java = {"Sneha", "Priya", "Rohan", "Neha", "Kiran"}

print("Both courses:", python & java)
print("Only one course:", python ^ java)
''',

    "set22.py": '''e1 = {"Python", "Java", "SQL", "Git", "HTML"}
e2 = {"Python", "C++", "SQL", "Docker", "Git"}

print("Common skills:", e1 & e2)
print("Employee 1 only:", e1 - e2)
print("Employee 2 only:", e2 - e1)
print("All skills:", e1 | e2)
''',

    "set23.py": '''books = {"Python Basics", "Java Programming", "Data Structures", "DBMS"}
requested = {"Python Basics", "DBMS", "Operating Systems", "AI Basics"}

print("Available requested books:", books & requested)
''',

    "set24.py": '''day1 = {101, 102, 103, 104, 105}
day2 = {104, 105, 106, 107, 108}

print("Unique visitors:", day1 | day2)
print("Returning visitors:", day1 & day2)
print("First day only:", day1 - day2)
print("Second day only:", day2 - day1)

category1 = {"Laptop", "Mouse", "Keyboard", "Monitor"}
category2 = {"Keyboard", "Monitor", "Printer", "Scanner"}

print("Common products:", category1 & category2)
''',

    "set25.py": '''user1 = {"Amit", "Rahul", "Sneha", "Priya", "Kiran"}
user2 = {"Sneha", "Priya", "Rohan", "Neha", "Kiran"}

print("Mutual friends:", user1 & user2)
print("User 1 only:", user1 - user2)
print("User 2 only:", user2 - user1)
print("Total unique friends:", user1 | user2)
'''
}

for name, code in files.items():
    with open(name, "w") as f:
        f.write(code)

print("25 Python files created successfully!")