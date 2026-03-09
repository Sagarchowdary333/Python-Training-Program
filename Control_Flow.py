# Control Flow in Python
# --------------------------------------------------------------------------------------------------------

# Control flow is the order in which the code is executed. 
  # * It is used to control the flow of the program. 
  # * It is used to make decisions in our code. 
  # * It is used to repeat a block of code. 
  # * It is used to handle exceptions in our code.

# Conditional Clauses in Python :
# --------------------------------------------------------------------------------------------------------

# if statement :
# -------------------------------------------------------------------------------------------------------

# Age=18
# if Age>17:
#     print("You Can Vote...!") # if condition is true then this line will be executed.

# Age=16
# if Age>17:
#     print("You Can Vote...!") # if condition is false then this line will not be executed.

# else statement :
# -------------------------------------------------------------------------------------------------------

# Age=16
# if Age>17:
#     print("You Can Vote...!")
# else:
#     print("You cannot Vote...!")

# Age=int(input("Enter your Age: "))
# if Age>17:
#     print("You Can Vote...!")
# else:
#     print("You cannot Vote...!")


# elif statement :
# -------------------------------------------------------------------------------------------------------

# a=50

# if a>=100:
#     print("Executed if Block")
# elif a>=50:
#     print("Executed elif Block")
# else:
#     print("Executed else Block")

# Task: mark ---> out of 100
# 90-100 ---> O Grade
# 80-89 ---> A+ Grade
# 70-79 ---> A Grade
# 60-69 ---> B Grade
# 50-59 ---> C Grade
# 0-49 ---> Fail

# Solution: 
# a=int(input("Enter the Marks: "))
# if a>99:
#     print("O Grade")
# elif a>89:
#     print("A+ Grade")
# elif a>79:
#     print("A Grade")
# elif a>69:
#     print("B Grade")
# elif a>49:
#     print("C Grade")
# else:
#     print("Fail")

# nested if statement :
# --------------------------------------------------------------------------------------------------------

# a=int(input("Enter the Marks: "))
# if a>49:
#     if a>89:
#         print("A Grade")
#     elif a>79:
#         print("B Grade")
#     elif a>69:
#         print("C Grade")
# else:
#     if a>59:        
#         print("D Grade")
#     elif a>49:
#         print("E Grade")
#     else:
#         print("Fail")
    
