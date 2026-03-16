# DATA STRUCTURES : All the Data Structures are Iterable Objects.
#                >> A Data Structure is a way to store and organize data so it can be used efficiently.
#                >>  

# Slicing: Extracting a portion of a sequence.
#          Means taking a portion of a list, string, or any other sequence type. 
#          It allows you to extract a specific range of elements from the sequence. 
#          The syntax for slicing:
#                     iterableobject[start:stop:step]
#                     - start: The index where the slice starts (inclusive). If omitted, it defaults to 0.
#                     - stop: The index where the slice ends (exclusive). If omitted, it defaults to the length of the sequence.
#                     - step: The interval between elements in the slice. If omitted, it defaults to 1. 

# Example of slicing:

# A = "SAGAR CHOWDARY"
# print(A[6:]) # Output: 'CHOWDARY'
# print(A[:5]) # Output: 'SAGAR '
# print(A[6:14]) # Output: 'CHOWDARY'
# print(A[::2]) # Output: 'SGRCODR'
# print(A[1:10:2]) # Output: 'AA HW'

# LIST : List is used to store an ordered collection of items. 
#        Lists are mutable, meaning you can modify them after they are created. 
#        They can contain elements of different data types, including numbers, strings, and even other lists.

# list = [1, 2, 3,'HELLO','SAGAR','CHOWDARY']

# print(len(list)) # Output: 6
# print(list[4]) # Output: 'SAGAR'
# print(list[2:5]) # Output: [3, 'HELLO', 'SAGAR']
# print(list[0:7:2]) # Output: [1, 3, SAGAR]


# list = [1, 2, 3,'HELLO','SAGAR','CHOWDARY',11,22,33,44,66]

# list[10]=54
# print(list)  # OUTPUT: [1, 2, 3, 'HELLO', 'SAGAR', 'CHOWDARY', 11, 22, 33, 44, 54]
# list[10]+=1
# print(list)  # OUTPUT: [1, 2, 3, 'HELLO', 'SAGAR', 'CHOWDARY', 11, 22, 33, 44, 55]



# list.append(ele) : .append means adding a new element at the end.

# list = [1, 2, 3,'HELLO','SAGAR','CHOWDARY',11,22,33,44,55]

# list.append([4,5,6])
# print(list) # OUTPUT: [1, 2, 3, 'HELLO', 'SAGAR', 'CHOWDARY', 11, 22, 33, 44, 55, [4, 5, 6]]


# List.extend(ele): Adding of multiple elements at the end.

# list.extend([66,77,88,99])
# print(list) # OUTPUT: [1, 2, 3, 'HELLO', 'SAGAR', 'CHOWDARY', 11, 22, 33, 44, 55, 66, 77, 88, 99]

# List.Insert(Position, Value)

# list.insert(3, 4)
# print(list) # OUTPUT: [1, 2, 3, 4, 'HELLO', 'SAGAR', 'CHOWDARY', 11, 22, 33, 44, 55, 66, 77, 88, 99]

# List.remove(Ele)

# list.remove(4)
# print(list) # OUTPUT: [1, 2, 3, 'HELLO', 'SAGAR', 'CHOWDARY', 11, 22, 33, 44, 55, 66, 77, 88, 99]

# List.pop(Ele)

# list.pop(14)
# print(list) # OUTPUT: [1, 2, 3, 'HELLO', 'SAGAR', 'CHOWDARY', 11, 22, 33, 44, 55, 66, 77, 88]

# List.pop()

# list.pop()
# print(list) # OUTPUT: [1, 2, 3, 'HELLO', 'SAGAR', 'CHOWDARY', 11, 22, 33, 44, 55, 66, 77]

# List.sort() ---> Assending Order

list= [1, 2, 3,66,77,88,99,11,22,33,44,55,4,5,6,7,8,9]

# list.sort() 
# print(list)

# List.Sort(reverse=True) ---> Desending Order

# list.sort(reverse=True)
# print(list) # OUTPUT: [99, 88, 77, 66, 55, 44, 33, 22, 11, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# list.reverse()

# list.reverse()
# print(list) # OUTPUT: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99]

# List.clear()

# list.clear()
# print(list)  # OUTPUT: []

