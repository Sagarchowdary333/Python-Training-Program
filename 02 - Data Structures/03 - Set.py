# set: Set is a collection of unique elements.
#       It is unordered and unindexed.
#       It is mutable. (After creating the Set We can change/update)
#       It will not allows Duplicates.
#       unindexed means we cannot access the elements by index.



# Syntax: {ele1,ele2,ele3,ele4,...}

Set= {1,2,3,4,5,4,3,2,1,'Hello','Sagar'}
# print(Set) # OUTPUT: {1, 2, 3, 4, 5, 'Hello', 'Sagar'}

# print(Set[2]) # OUTPUT: TypeError: 'set' object is not subscriptable
# Because we cannot access the elements by index in Set

# for i in Set:
#     print(i) # OUTPUT: 1
#                      2
#                      3
#                      4
#                      5
#                      Hello
#                      Sagar 
# Because for loop is used to access the elements in Set.

# Inbuilt Methods in Set:

# .add(Ele) ---> Adding new element in Set at the end.

# Set.add('Chowdary')
# print(Set) # OUTPUT: {1, 2, 3, 4, 5, 'Hello', 'Sagar', 'Chowdary'}

# .remove(Ele) ---> Removing element from the set.

# Set.remove('Chowdary')
# print(Set) # OUTPUT: {1, 2, 3, 4, 5, 'Hello', 'Sagar'}

# .Clear() ---> Removing all the elements from the Set.

# Set.clear()
# print(Set) # OUTPUT: set() 

# .Union(set) ---> Union of two sets.

Set1= {1,2,3,4,5}
Set2= {4,5,6,7,8}
# print(Set1.union(Set2)) # OUTPUT: {1, 2, 3, 4, 5, 6, 7, 8}  

# .Intersection(set) ---> Intersection of two sets. It will return the common elements of two sets.

# print(Set1.intersection(Set2)) # OUTPUT: {4, 5}

# .Difference(set) ---> Difference of two sets. It will return the elements which are not common in two sets.
# print(Set1.difference(Set2)) # OUTPUT: {1, 2, 3}
# print(Set2.difference(Set1)) # OUTPUT: {6, 7, 8}