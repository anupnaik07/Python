# def hello():
#     print("This is the calling function")
#     print("This is the good method to call a function")
# hello() #calling the function

# def addition(a,b): #here in bracket addition(here are the parameters that get called when needed)
#     sum = a + b
#     print(sum)
# addition(13,25)

    # PRIMITIVE APPROACH
# a = 121
# copy = a
# rev = 0
    
# while a > 0:
#     rev = rev * 10 + a%10
#     a = a // 10     
# if copy == rev:
#     print("It is the palindrome number.")
# else : 
#     print("It is not the palindrome number.")
        
        
        
    # FUNCTIONAL APPROACH 

# Q) write a code where a number is pallindrome or not by using function method.
# def pallindrome_checker(a):
#     copy = a
#     rev = 0
    
#     while a > 0:
#         rev = rev * 10 + a%10
#         a = a // 10
        
#     if copy == rev:
#         print("It is the palindrome number.")
#     else : 
#         print("It is not the palindrome number.")

# pallindrome_checker(121)
# pallindrome_checker(124)
# pallindrome_checker(545)



    # PARAMETERS & ARGUMENTS : 

# parameters are the values you accept while calling the function.
# arguments are the values you provide to parameters while calling the function.


    # POSITIONAL ARGUMENT : 

# def multiply(a,b,c,d):
#     print(a*b*c*d)
# multiply(2,5,4,6)


    # DEFAULT ARGUMENT :

#   """and if you want the d as a separate parameter then it will give you error plus this is the wrong format to wirte...
#     here if you provide a parameter value that is the default value...
#     why when you provide a parameter the value then the next parameter should be given like d = 14, e = 56 like this...
#     and the most important thing here is that when you provide a value for "c" like c = 5 then the value will change...
#     but if you want the next paramete should given the you can add before the setting value just like this (a,b,d,c=12)."""
# def addition(a,b,c=12): 
#     print(a+b+c)
# addition(5,12)


    # KEYWORD ARGUMENT : 

# here if you want different value for different parameter you can use keyword argument and if once you used the keyword argument then you must use for the next parameter
# def subtraction(a,b,c):
#     print(b-a-c)
# subtraction(12,c=15,b=70)




    # EXERCISES 
    
# Q1) Create a function that accepts three numbers and returns their average.

# def average(a,b,c):
#     print((a+b)/c)
# average(12,8,2)


# Q2) Create a function that calculates the area of a rectangle.

# def rectangle_area(l,b):
#     area = l * b
#     print(area)
# rectangle_area(12,12)


# Q3) Create a function that converts Celsius into Fahrenheit

# def c_f_conversion(c):
#     f = c * (9/5) + 32
#     print(f)
# c_f_conversion(5)


# Q4) Create a function that returns the largest of three numbers.

# def largest_no(a,b,c):
#     if a > b and a > c:
#         print(f"{a} is largest number between {a,b,c}")
#     elif b > a and b > c:
#         print(f"{b} is largest number between {a,b,c}")
#     else :
#         print(f"{c} is largest number between {a,b,c}")
# largest_no(5,6,4)


# Q5) Create a function that calculates the factorial of a number.

# def factorial(a):
#         fact = 1    
#         for i in range(1, a+1):
#             fact *= i
#         print(fact) 
# factorial(5)


# Q6) Create a function using default arguments to calculate student marks.

# def marks(m):
#     if m >= 75 and m <=100:
#         print(f"{m} you got an A rank")
#     elif m >= 60 and m <= 74:
#         print(f"{m} you got an B rank")
#     elif m >= 50 and m <= 59:
#         print(f"{m} you got an C rank")
#     elif m >= 40 and m <= 49:
#         print(f"{m} you got an D rank")
#     elif m <= 35:
#         print("You have failed in the exam")
#     else : 
#         print("wrong marks")
# marks(45)


# Q7) Create a function using *args to calculate the sum of multiple numbers.

# def sum_all(*args):
#     return sum(args)
# print(sum_all(1,2,3,4,5,6,7))
