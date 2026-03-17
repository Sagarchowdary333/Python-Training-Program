# Loops In Python
# --------------------------------------------------------------------------------------------------------
# It is used to execute a block of code repeatedly until a certain condition is met. 
# There are two types of loops in Python.
# for loop. 
# while loop.



# While Loop : It is going to execute the block of Code as long as the condition becoumes True. 
#              When the condition becomes False then it will stop executing the code.

# When we will use while loop ? ---> When we don't know the number of iterations or 
#                                    When we want to execute a block of code until a certain condition is met.

# while True:
#     print("Sagar Chowdary...!")
#     print("I am a DevOps Engineer...!")
#     print("--------------------------------")

    # Output:
        # Sagar Chowdary...!
        # am a DevOps Engineer...!
        # --------------------------------
# No of Execution : Infinite times.

# a = 3
# while a > 0:
#     print("Sagar Chowdary...!")
#     print("I am a DevOps Engineer...!")
#     print("--------------------------------")
#     a = a - 1

    # Output:
        # Sagar Chowdary...!
        # I am a DevOps Engineer...!
        # --------------------------------
        # Sagar Chowdary...!
        # I am a DevOps Engineer...!
        # --------------------------------
        # Sagar Chowdary...!
        # I am a DevOps Engineer...!
        # --------------------------------


# LuckyNumber = 3
# NotFound=True
# while NotFound:
#     inputNumber = int(input("Enter a number : "))
#     if inputNumber == LuckyNumber:
#         print("U Found the Lucky Number...!")
#         NotFound = False
#     else:
#         print("Try Again...!")




# For Loop : It is used to iterate over a sequence (like a list, tuple, string) or other iterable objects.
#             It executes a block of code for each item in the sequence.

# when the sequence is exhausted, the loop stops executing the code.

# when we will use for loop ? ---> when we know the number of iterations or when we want to iterate over a sequence.

# Syntax : for variable in sequence:
#                block of code to be executed
# 
# Sequence(Iterable Object) : If an object is able to return its own members one by by, then it is called as Sequence or Iterable Object.
#                            Ex: List, Tuple, String, Set, Dictionary.

# Index Number : It is used to identify the position of an element in a sequence. It starts with 0 and ends with n-1, 
#                where n is the total number of elements in the sequence.
#                In the list [1, 2, 3], the index of element 1 is 0, the index of element 2 is 1, and the index of element 3 is 2.
#                Ex : A = [Sagar, Chowdary, DevOps, Engineer]
#                Index :     0       1         2        3
#                A[0] = Sagar
#                A[1] = Chowdary
#                A[2] = DevOps
#                A[3] = Engineer

# Lenght Of Sequence : It is used to find the total number of elements in a sequence. It is denoted by len() function.
#                     Ex : A = [Sagar, Chowdary, DevOps, Engineer]
#                     len(A) = 4

# str = "Sagar"
# for char in str:
#     print(char)

#     # Output:
#         # S
#         # a
#         # g
#         # a
#         # r

#     print("Sagar Chowdary...!")
#     print("I am a DevOps Engineer...!")
#     print("--------------------------------")

    # Output:
        # S
        # Sagar Chowdary...!
        # I am a DevOps Engineer...!
        # --------------------------------
        # a
        # Sagar Chowdary...!
        # I am a DevOps Engineer...!
        # --------------------------------
        # g
        # Sagar Chowdary...!
        # I am a DevOps Engineer...!
        # --------------------------------
        # a
        # Sagar Chowdary...!
        # I am a DevOps Engineer...!
        # --------------------------------
        # r
        # Sagar Chowdary...!
        # I am a DevOps Engineer...!
        # --------------------------------

#   for char in range(5):
#       print("Sagar")
#       print("----------")

# for char in range(1, 5):
#     print(char)

# for char in range(1, 10, 2):
#     print(char)

# Range Function : It is used to generate a sequence of numbers. It takes three parameters, start, stop and step.
#                  start : It is the starting point of the sequence. It is optional and default value is 0.
#                  stop : It is the ending point of the sequence. It is mandatory.
#                  step : It is the increment value of the sequence. It is optional and default value is 1.
#                  Ex : range(lenght) ---> range(5) = 0, 1, 2, 3, 4
#                       range(Start, Stop) --->range(1, 5) = 1, 2, 3, 4
#                       range(start, stop, step) ---> range(1, 10, 2) = 1, 3, 5, 7, 9
#                                                     range(10, 1, -1) = 10, 9, 8, 7, 6, 5, 4, 3, 2

#                       print(list(range(5))) ---> [0, 1, 2, 3, 4]
#                       print(list(range(1, 5))) ---> [1, 2, 3, 4]
#                       print(list(range(1, 10, 2))) ---> [1, 3, 5, 7, 9]
#                      print(list(range(10, 1, -2))) ---> [10, 8, 6, 4, 2]

# print(list(range(11)))

# Control statements in loops at Python.
# --------------------------------------------------------------------------------------------------------
# control statements are used to control the flow of the loop. There are three control statements in Python.

# break : It is used to terminate the loop.

# Ex:
# i= 0                OUTPUT : 0
# while i < 10:                1
#     if i == 5: --->          2
#         break                3
#     print(i)                 4
#     i = i + 1

# SecretNumber = 3
# while True:
#     inputNumber = int(input("Enter a number : "))
#     if inputNumber == SecretNumber:
#         break
#     else:
#         print("Try Again...!")

# for i in range(10):  OUTPUT : 0
#     if i == 5:                1
#         break  --->           2
#     print(i)                  3
#                               4

# continue : It is used to skip the current iteration and move to the next iteration.

# Ex:
# for i in range(10):   OUTPUT : 0
#     if i == 5:                 1
#         continue               2
#     print(i)                   3
#                                4
#                                6
#                                7
#                                8
#                                9

# i= 0                  OUTPUT : 0
# while i < 10:                  1
#     if i == 5:                 2
#         continue               3
#     print(i)                   4
#     i = i + 1


# i= 0                  OUTPUT : 0
# while i < 100:                 1
#     if i > 25:                 2
#         continue               3
#     print(i)                   4
#     i = i + 1                  5

# pass : It is used as a null statement, i.e., it does nothing when executed.
