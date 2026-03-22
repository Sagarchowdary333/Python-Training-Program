# Funtions: It is a block of code that performs a specific task and can be reused multiple times in a program.
#           It is a collection of statements that perform a specific task and can be called multiple times in a program.
#           It is a way to break down a complex task into smaller, more manageable parts.

# Syntax:
#        def FunName():
#            block of code
#        FunName() ---> calling the function

# def Training():
#     print("Functions in Python")
# Training() 

# OUTPUT: Functions in Python

# def Training():
#     print("Functions in Python")
# Training()
# Training()

# OUTPUT: Functions in Python
#         Functions in Python
# Because the function is called multiple times.


# Parameters: Parameters are the variables created inside the function without a value assigned to them.

#            Parameters
#                ^
#                |
#                |
def Training(Name, Role):
    print("Trainee Name:", Name)
    print("Role:", Role)

Training("Sagar", "DevOps Engineer")
#                    ^
#                    |
#                    |
#                Arguments

# OUTPUT: Trainee Name: Sagar
#         Role: DevOps Engineer