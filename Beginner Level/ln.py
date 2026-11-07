# sherNYC = 12

# camel case 
# sheriyansXNyc = 12 

# pascal case 
# sheriyansXNyc = 23

# # snake case
# sherians_x_nyc = 45

# ________________________________________________________
# boolean 
# a = True 
# b  = False
# print(type(a))
# ________________________________________________________

# a = None
# print(type(a))
# ________________________________________________________

# unicode (ascii value = "ord")
# a = "h"
# print(ord(a))
# ________________________________________________________

# indexing positive and negative
# a = "anup"
# print(a[3], a[-2])
# ________________________________________________________

# string slicing 
# [default=0: default=size of array: step] = [::2] = CLEE
# a = "COLLEGE"
# print(a[0:7:2])

# QUS 
# a = "Hello how are you"
# # how 
# print(a[6:9:1])
# # you
# print(a[14:17:1])
# # Hello
# print(a[:5:1])
# ________________________________________________________

# C3 : TYPE CONVERSION 
# int() | float() | str() |
# a = 12.9788
# print(a)
# a = int(a)
# print(type(a))
# b = float(a)
# print(type(b))
# print(type(float(b)))  


# a = 123
# b = 34.6
# c = 12 + 3j
# d = True

# a = str(a)
# b = str(b)
# c = str(c)
# d = str(d)

# boolean
# 7 False values: False | 0 | 0.0 | "" | [] | () | {} 
# after this 7 false values all are the TRUE values for every other datatype
# a = 12 # True
# b = 0 # False
# c = 12.4 #True
# d = 0.0 # False
# e = "" # False
# f = "hello" # True

# print(bool(a))
# print(bool(b))
# print(bool(c))
# print(bool(d))
# print(bool(e))
# print(bool(f))
# ________________________________________________________

# C4 : Input Output & Operators
# name = "Anup"
# age = 21
# print(f"My name is {name} and my age is {age}") #f = formated string that uses variables in {} 
# print("my name is ", name, "my age is ", age) #same as the upper one but there is no formated string so we use comma(,) to separate them

# name = str(input("Enter your name : "))
# age = int(input("Enter your age : "))
# print(f"Hello there {name} your age is {age}")

# ARITHMETIC OPERATORS :
# numbers : int , float, complex
# (+, - , / , // (floor division = converts float into int) , * ,** (power operator),% (modulo operator = remainder))
# a = 10
# b = 20
# c = 12
# d = 56
# print(a + b + c + d + 34 + 64)

# // (floor division = converts float into int) 
# a = 12
# print(a//2)

""""
() : brackets
** : exponent (right to left : 2**2**3 = 2**(2**3)))
* / // % : multiplication | division | floor division | modulus
+ - : addition | subraction
"""
"""
print(3 + 4 * 2)
print(15 // 4 + 15 % 4)
print(3 + 2 ** 2 * 5 - 1)
"""
"""" COMPARISON OPERATORS
(== , > , < , >=, <=, !=) results are always in boolean values
print(16 == 16)
print(12 > 14)
print(12 < 45)
print(12 >= 12)
print(45 <= 56)
print(23 != 23)
"""
# ________________________________________________________

""" LOGICAL OPERATORS
AND(one false all false ) OR(one true every true) AND NOT(interchange false to true & true to false)
print (12>10 and 34==34 and 45==45) 
"""
# ________________________________________________________

"""ASSIGNMENT OPERATORS
+= , -=, *=, /= , //=, %=, **=
a = 10
a += 10
"""
# ________________________________________________________