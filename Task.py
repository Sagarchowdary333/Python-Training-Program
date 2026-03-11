#----------TASK 3----------

# Numbers = [10, 20, 30, 20, 40]
# print("Original list:", Numbers)

# Numbers.append(50)
# print("After append:", Numbers)

# Numbers.extend([60, 70])
# print("After extend:", Numbers)

# Numbers.insert(1, 15)
# print("After insert:", Numbers)

# Numbers.remove(20)
# print("After remove:", Numbers)

# Numbers.pop()
# print("After pop():", Numbers)

# Numbers.pop(3)
# print("After pop(3):", Numbers)

# Numbers.clear()
# print("After clear:", Numbers)

# Numbers.sort()
# print("Ascending:", Numbers)

# Numbers.sort(reverse=True)
# print("Descending:", Numbers)

# Numbers.reverse()
# print("After reverse:", Numbers)

# print("Index of 30:", Numbers.index(30))

# print("Count of 20:", Numbers.count(20))

# TUPLES

# T = (1, 2, 3, 2, 4)
# print("Tuple:", T)

# print("Index of 2:", T.index(2))

# print("Count of 2:", T.count(2))

# T = (1, 2, 3, 4)
# a, b, c, d = T
# print("Unpacked values:", a, b, c, d)

# S = {1, 2, 3, 2, 4}
# print("Set:", S)

# S.add(5)
# print("After add:", S)

# S.remove(3)
# print("After remove:", S)

# S.clear()
# print("After clear:", S)

# S2 = {4, 5, 6}
# print("Union:", S.union(S2))

# print("Intersection:", S.intersection(S2))

# print("Difference:", S.difference(S2))

# Student = {
#     "Name": "Sagar",
#     "Age": 23,
#     "Course": "Python"
# }

# # print("Dictionary:", Student)

# # print("Keys:", Student.keys())

# # print("Values:", Student.values())

# Student.pop("Age")
# print("After pop:", Student)

#----------TASK 4----------

# def Training():
    # print("Functions in Python")

# Training()

# To define a function in Python, you use the def keyword followed by the function name and parentheses. Inside the parentheses, you can specify parameters that the function can accept. After the parentheses, add a colon and start a new indented block for the function body.

# EX : def function_name(parameter1, parameter2, ...):
# Function body
# Perform some operations

# >>> Parameters and Arguments:

# def sum_numbers(x, y):
#     total = x + y
#     print("Total:", total)

# sum_numbers(6, 4)

# >>> Positional Arguments:

# def Trainee(Name, Role):
#     print("Trainee Name:", Name)
#     print("Role:", Role)

# Trainee("Sagar", "DevOps Engineer")

# >>> Keyword Arguments:

# def Trainee(Name, Role):
#     print("Trainee Name:", Name)
#     print("Role:", Role)

# Trainee(Role="DevOps Engineer", Name="Sagar")

# >>> Default Arguments:   

# def Greet_Trainee(Name="Trainee"):
#     print("Welcome", Name)

# Greet_Trainee()
# Greet_Trainee("Sagar")

# Variable Length Arguments

# def Numbers(*values):
#     for i in values:
#         print(i)

# Numbers(5, 10, 15, 20)

# >>> Return Keywords

# def square(n):
#     result = n * n
#     return result

# value = square(6)
# print("Square value:", value)

# ---------- Task 5 ----------

# String Operations:
# -----------------------
# Concatenation

# str1 = "Sagar"
# str2 = "Chowdary"

# result = str1 + " " + str2
# print(result)

# Repetition

# text = "Sagar Chowdary "
# print(text * 3)

# Built-in String Methods:
# ------------------------

# name = "sagar chowdary"

# .upper()
# print(name.upper())

# .lower()
# print(name.lower())

# .title()
# print(name.title())

# capitalize()
# print(name.capitalize()) 

# Whitespace Removal Methods: 
# --------------------------

# name = "   Sagar Chowdary   "

# .strip()
# print(name.strip())

# .lstrip()
# print(name.lstrip())

# .rstrip()
# print(name.rstrip())

# Other String Methods:
#------------------

# from os import name


# Name = "Vidya Sagar"

#  .replace(old, new)
#  print(Name.replace("Vidya", "Kota"))

#  .split(breakChar) → splits string into multiple substrings stored in a list
#  print(Name.split(" "))

#  .join(iterable) → joins elements of iterable into a string
#  

# Name = "Sagar"
# Age = 23

# print(f"My name is {Name} and I am {Age} years old")



# ---------- Task 6 ----------

# Errors and handle exceptions in Python
# -----------------------------------------

# ZeroDivisionError & ValueError
# ---------------------------------

# EX :
      # try:
      #     a = int(input("Enter first number: "))
      #     b = int(input("Enter second number: "))
            
      #     result = a / b
      #     print("Result:", result)

      # except ZeroDivisionError:
      #     print("Cannot divide by zero")

      # except ValueError:
      #     print("Invalid input. Please enter numbers only")

# Try & Except & Finally
# ------------------------------------

# EX :
      # try:
      #     num = int(input("Enter a number: "))
      #     print("Number entered:", num)

      # except ValueError:
      #     print("Input should be a number")

      # finally:
      #     print("Executed")



# File Handling in Python
# ------------------------------------ 

# file operations in Python.
# --------------------------

# create a file and write text
    # file = open("data.txt", "w")
    # file.write("This is my first file.\n")
    # file.close()

# Append content
    # file = open("data.txt", "a")
    # file.write("This is an appended line.\n")
    # file.close()

# Read Entire File
    # file = open("data.txt", "r")
    # content = file.read()
    # print(content)
    # file.close()

# Read the file line by line
    # file = open("data.txt", "r")
    # lines = file.readlines()
    # for line in lines:
    #     print(line)
    # file.close()