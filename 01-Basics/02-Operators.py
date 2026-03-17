# Arithmetic

# a = 33
# b = 33
# print(a+b)
# print(a-b)
# print(a*b)
# a =333
# b = 13
# print(a/b) # Answer = 25.615384615384617 
# a =333
# b = 13
# print(a//b) # Answer will be 25 because it will ignore all the decimal part and keep integer part only.
# print(a//b)
# print(a%b) # Answer will be 8 because it gives the Reminder Value.
             # Ex : 333%13 ---> 333/13=25.6 ---> 13*25=325 ---> 333-325=8
             # Ex : 13%333 ---> 13/333=0.03 ---> 333*0=0 ---> 13-0=13
# print(a**2) # Answer will be 1089 (which gives the result of a raised to the power of b).
            # Ex : 33**2 ---> 33*33=1089
            # Ex : 33**3 ---> 33*33*33=35937
            # Ex : 33**0 ---> 1 (Any number raised to the power of 0 will be 1)



# Comparison

a = 33
b = 13
# print(a==b) # Answer False
# print(a!=b) # Answer True
# print(a>b) # Answer True
# print(a<b) # Answer False
# print(a>=b) # Answer True
# print(a<=b) # Answer False



# Logical

a = True
b = False
# print(a and b) # Answer False because both a and b should be True to get the answer True.
# print(a or b) # Answer True because at least one of a or b should be True to get the answer True.
# print(not a) # Answer False because a is True and not operator will give the opposite value.
# print(not b) # Answer True because b is False and not operator will give the opposite value.
# print(not not a) # Answer True because not a is False and not False is True.
# print(a and not b) # Answer False because a is True and not b is False and both should be True to get the answer True.
# print(not a or b) # Answer False because not a is False and b is False and both should be True to get the answer True.



# Assignment

# a = 10
# a += 5  # Equivalent to a = a + 5
# print(a)  # Output: 15
# a -= 3  # Equivalent to a = a - 3
# print(a)  # Output: 12
# a *= 2  # Equivalent to a = a * 2
# print(a)  # Output: 24
# a /= 4  # Equivalent to a = a / 4
# print(a)  # Output: 6.0
# a //= 2  # Equivalent to a = a // 2
# print(a)  # Output: 3.0
# a %= 2  # Equivalent to a = a % 2
# print(a)  # Output: 1.0
# a **= 3  # Equivalent to a = a ** 3
# print(a)  # Output: 1.0



# Bitwise
#- - - - - 256 128 64 32 16 8 4 2 1
a = 5  # In binary: 0000 0101 
# Binary numbers are calculated by adding the required powers of 2 to get the given number.We write 1 in the positions that are used and 0 in the remaining positions.
# Ex : 256 128 64 32 16 8 4 2 1
     # 5 in binary is 0000 0101 ---> 4 + 1 = 5 Keeping the values of the positions where there is 1 in the binary representation and adding numbers 4 and 1 gives us the original number 5.

print(10 & 9) # Answer will be 8 because in binary 10 is 0000 1010 and 9 is 0000 1001 and the bitwise AND operator (&) compares each bit of the two numbers and returns a new number where each bit is set to 1 only if both corresponding bits of the original numbers are 1. In this case, the result is 0000 1000, which is 8 in decimal.
print(10 | 9) # Answer will be 11 because in binary 10 is 0000 1010 and 9 is 0000 1001 and the bitwise OR operator (|) compares each bit of the two numbers and returns a new number where each bit is set to 1 if at least one of the corresponding bits of the original numbers is 1. In this case, the result is 0000 1011, which is 11 in decimal.
print(10 ^ 9) # Answer will be 3 because in binary 10 is 0000 1010 and 9 is 0000 1001 and the bitwise XOR operator (^) compares each bit of the two numbers and returns a new number where each bit is set to 1 only if the corresponding bits of the original numbers are different. In this case, the result is 0000 0011, which is 3 in decimal.
print(10 >> 3) # Answer will be 1 because in binary 10 is 0000 1010 and the right shift operator (>>) shifts the bits of the number to the right by the specified number of positions. In this case, shifting the bits of 10 to the right by 3 positions results in 0000 0001, which is 1 in decimal.
print(10 << 1) # Answer will be 20 because in binary 10 is 0000 1010 and the left shift operator (<<) shifts the bits of the number to the left by the specified number of positions. In this case, shifting the bits of 10 to the left by 1 position results in 0001 0100, which is 20 in decimal.
print(10 << 3) # Answer will be 80 because in binary 10 is 0000 1010 and the left shift operator (<<) shifts the bits of the number to the left by the specified number of positions. In this case, shifting the bits of 10 to the left by 3 positions results in 0010 1000, which is 80 in decimal.
print(~10) # Answer will be -11 because in binary 10 is 0000 1010 and the bitwise NOT operator (~) inverts all the bits of the number. In this case, inverting the bits of 10 results in 1111 0101, which is -11 in decimal (using two's complement representation for negative numbers).
