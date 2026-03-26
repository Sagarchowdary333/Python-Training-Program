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

# INBUILT FUNCTIONS: Inbuilt functions are the functions that are already provided by Python.
#                    Example: print(), input(), len(), type().

# USER DEFINED FUNCTIONS: User defined functions are the functions that are created by the programmer to perform a specific task.

# print(input())

# Parameters: Parameters are the variables created inside the function without a value assigned to them.

#            Parameters
#                ^
#                |
#                |
# def Training(Name, Role):
#     print("Trainee Name:", Name)
#     print("Role:", Role)

# Training("Sagar", "DevOps Engineer")
#                    ^
#                    |
#                    |
#                Arguments

# Arguments: Arguments are the values passed to the function when it is called.

# OUTPUT: Trainee Name: Sagar
#         Role: DevOps Engineer

# def Addition(A,B):
#     print(A+B)

# Addition(33,33) ---> 66



# Positional Arguments: Positional arguments are the arguments that are passed to the function in the same order as they are declared in the function definition.
# Order matters in positional arguments.

# def Positional(A,B):
#     print(A+B)
#     print("A:"+str(A))
#     print("B:"+str(B))

# Positional(33,33)
# Positional("Hi","Sagar") # OUTPUT: 66
                           #         A:Hi
                           #         B:Sagar
                           #         HiSagar
                           #         A:Hi
                           #         B:Sagar



# Keyword Arguments: Keyword arguments are the arguments that are passed to the function using the name of the parameter.
#                    Order Does Not matter in keyword arguments.

# def Keyword(A,B):
#     print(A+B)
#     print("A:"+str(A))
#     print("B:"+str(B))

# Keyword(33,33)
# Keyword(A=33,B=33)
# Keyword(B="Sagar",A="Hi")

# OUTPUT: 66
#         A:33
#         B:33
#         66
#         A:33
#         B:33
#         HiSagar
#         A:Hi
#         B:Sagar



# Default Arguments: Assinging a default values to the Parameters.
#                    Default arguments are the arguments that are passed to the function if no value is passed to them.
#                    Default arguments are declared after the positional & keyword arguments.
#                    Default arguments are declared after the variable length arguments.

# def Default(A,B,C=33):
#     print(A*B*C)

# Default(33,33) # C value is default ---> C value already assigned in Parameters. Remaining values of A & B are passed to function.
                 # OUTPUT: 35937

# def Default(A,B,C=33):
#     print(A*B*C)

# Default(3,33,333) # C value has changed in function. so the C value in Parameters will be ignored and the updated value will be printed.
                    # OUTPUT: 32967



# Variable Length Arguments: When you don't know the number of arguments that are passed to the function, you can use variable length arguments.
#                            Variable length arguments are the arguments that are passed to the function as a list.
#                            Variable length arguments are declared after the positional & keyword & default arguments.
#                           

# def variable(*Parameters):
#     print(Parameters)

# variable(33,33,33) # OUTPUT: (33, 33, 33)


# def Variable(A,B,*C):
#     print(A+B+sum(C))
#     print(A)
#     print(B)
#     print(C)

# Variable(33,33,33,33,33) # OUTPUT: 165
#                          #         33
#                          #         33
#                          #         (33, 33, 33)


# def Variables(*A):
#     print(sum(A))

# Variables(33,33,33) # OUTPUT: 99

# # Without using Sum Function
# def Variables(*A):
#     Total=0
#     for i in A:
#         Total+=i
#     print(Total)

# Variables(3,3,3) # OUTPUT: 9



# RETURN KEYWORD: Return keyword is used to return a value from a function.
#                 It is used to stop the execution of the function and return the value to the caller.

# def Keyword():
#     print("Hi")
#     print("Hello")
#     return
#     print("Bye")

# Keyword() # OUTPUT: Hi
#           #         Hello


# def Keyword():
#     print("Hi")
#     print("Hello")
#     return "Sagar"
#     print("Bye")

# print(Keyword())---> # OUTPUT: Hi
#                      #         Hello
#                      #         Sagar
# a=Keyword()          
# print(a)        ---> # OUTPUT: Hi             
#                      #         Hello
#                      #         Sagar
# print(a+" Chowdary") # OUTPUT: Hi
#                      #         Hello
#                      #         Sagar Chowdary
# Keyword()       ---> # OUTPUT: Hi
#                      #         Hello
# def Keyword():
#     print("Hi")
#     print("Hello")
#     return 
#     print("Bye")

# A=Keyword()
# print(A)    ---> # OUTPUT: Hi
#                  #         Hello
#                  #         None

# def Keyword():
#     print("Hi")
#     print("Hello")
#     print("Bye")

# A=Keyword()
# print(A)    ---> # OUTPUT: Hi
#                  #         Hello
#                  #         Bye
#                  #         None

