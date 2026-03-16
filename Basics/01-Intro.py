# print(123)
# print(456)

# the below line of code is Wrong
# Print(789)

''' Company Name : Stackly
    Employee Name : Sagar Chowdary
    Domine : DevOps Enginneer '''

# a=10        or  Emp_ID=12345
# print(a)        print(Emp_ID)

# the below line of code is Wrong
# print=10
# print(print)

# a=10
# a=20
# print(a)
# Answer will be 20 because latest assigned value will be consider.

# a=10 ---> Integer
# b=10.5 ---> Float
# c="Sagar" or Str1='Sagar'
# str2='Chowdary'

# print(type(a))
# Answer will be <class 'int'> the inner most called function will be executed first.
# print(type(b))
# Answer will be <class 'float'> the inner most called function will be executed first.

# print(a+b) ---> 20.5
# print(a*2) ---> 20
# print(a+c) ---> Error because we can't add int and str
# print(str1+str2) ---> SagarChowdary
# print(str1*2) ---> SagarSagar
# print(str1*2+str2) ---> SagarSagarChowdary

# input() function is used to take input from user. By default it will consider the value as string.
# ----------------------------------------------------------------------------------------------------

# a=input()
# print(a)
# print(a+40) ---> Error because we can't add int and str
# print(a*2) ---> 1010 because input function will consider the value as string by default. if we want to consider the value as integer then we have to use int() function.

# a=int(input("Enter: "))
# print(a+40)

# Age=int(input("Enter your Age: "))
# print("You Can Vote...!")
# print("You cannot Vote...!")
