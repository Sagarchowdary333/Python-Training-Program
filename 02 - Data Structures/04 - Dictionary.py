# Dictionary: Dictionary is used to store the data in the form of key-value pair.
#             Dictionaries are Mutable. (After creating the Dictionary We can change/update)
#             Dictionaries are Unordered. (We cannot access the elements by index)
#             Dictionaries are Indexed. (We can access the elements by index)
#             Dictionaries allows Duplicates. (We can have duplicate keys in the Dictionary)

# Syntax: {key1:value1,key2:value2,key3:value3,...}


Details= {"Name":'Sagar',"Age":'23',"Domain":'DevOps Engineer'}

# print(Details)
# OUTPUT : {'Name': 'Sagar', 'Age': '23', 'Domain': 'DevOps Engineer'}

# print(Details["Name"]) # OUTPUT: Sagar  ---> Accessing the element by key

# Details["Age"]="24"  ---> Update
# print(Details)
# OUTPUT : {'Name': 'Sagar', 'Age': '24', 'Domain': 'DevOps Engineer'}


# Details["Company"]="Stackly" ---> Add
# print(Details)
# OUTPUT : {'Name': 'Sagar', 'Age': '24', 'Domain': 'DevOps Engineer', 'Company': 'Stackly'}

# Inbuilt Methods:

# .keys() ---> Returns the keys of the dictionary.
# .values() ---> Returns the values of the dictionary.
# .items() ---> Returns the key-value pairs of the dictionary.

# print(Details.keys()) # OUTPUT : dict_keys(['Name', 'Age', 'Domain'])

# print(Details.values()) # OUTPUT : dict_values(['Sagar', '24', 'DevOps Engineer'])

# print(Details.items()) # OUTPUT : dict_items([('Name', 'Sagar'), ('Age', '24'), ('Domain', 'DevOps Engineer')])

# .pop("key") ---> Removing the element by key

# print(Details.pop("Age")) # OUTPUT : 23

# print(Details) # OUTPUT : {'Name': 'Sagar', 'Domain': 'DevOps Engineer'}

# print(Details.get("Age")) # OUTPUT : None

# print(Details.popitem()) # OUTPUT : ('Domain', 'DevOps Engineer')

# print(Details) # OUTPUT : {'Name': 'Sagar'}

# for loop ---> It is used to iterate over a sequence (like a list, tuple, string) or other iterable objects.
#              It executes a block of code for each item in the sequence.

for i in Details:
    print(i) # OUTPUT : Name
             # Age
             # Domain

for i in Details:
    print(Details[i]) # OUTPUT : Sagar
                      # 23
                      # DevOps Engineer