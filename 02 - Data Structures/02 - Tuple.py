# Tuple: Tuple is used to store Permanent data. The Data we would not want to change in future.
#        Tuples are faster than the List.
#        Tuples are Immutable. (After creating the Tuple We cannot change/update)
#        Tuples are allows Duplicates.
#        Tuples are ordered.
#  

# Tuple= [1,2,3,4,5,4,3,2,1,'Hello','Sagar']

# .insert(Ele) ---> Finds the index number for the elements.

# print(Tuple.index(4)) # OUTPUT: 3


# .Count(Ele) ---> No of Occurance

# print(Tuple.count(3)) # OUTPUT: 2

# packing: If we want create Tuple in python, we can create it without parenthesis.
#         P

Tuple= 1,2,3,4,5,4,3,2,1,'Hello','Sagar'

print(Tuple) # OUTPUT: (1, 2, 3, 4, 5, 4, 3, 2, 1, 'Hello', 'Sagar')

# unpacking: If we want create Tuple in python, we can create it without parenthesis.
#            Unpacking means assigning values to variables from a tuple.

Tuple= 1,2,3,4,5,4,3,2,1,'Hello','Sagar'
Tuple1= (6,7,8,9,10,11,12,13,14,'Hello','Sagar')

a,b,c,d,e,f,g,h,i,j,k=Tuple

print(c) # OUTPUT: 3
