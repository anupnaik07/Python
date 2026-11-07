# c6 : Loops 
"""
range(start , stop , step) it is also used in strig slicing

ranges : 
10 - 100
23 - 56
0 - 45
"""
# range(10,101,1)
# range(23,57,1)
# range(46)

    # for table ; 
# n = int(input("Enter a number for its table: "))

# for i in range(n,(n*10)+1,n):
#     print(i)

    # for strings :
# a = "students"

# for i in a:
#     print(i)

    # in indexing format 
# for i in range(0,len(a)):
#     print(f"{i} : {a[i]}") 

    # break | continue | else

# for i in range(1,11):
#     if i ==5 or i ==6 or i==7:
#         continue
#     print(i)

    # for : else (attached to for)

# for i in range(1,11):
#     if i == 45:
#         break
#     print(i)
# else : 
#     print("No break was encountered.")

    #Q1) print hello world n times
# n = int(input("enter your number to print n times : "))

# for i in range(n):
#     print("dev.an")

    #Q2) print natural numbers n times
# n = int(input("Enter a number : "))

# for i in range(1,n+1):
#     print(i)

    #Q3) print natural numbers n times in reverse format
# n = int(input("Enter a number : "))

# for i in range(n,0,-1):
#     print(i)

    # Q4) print multiplication table given by user
# n = int(input("Enter a table number : "))

# for i in range(1,11):
#     print(f"{n} x {i} = {n*i}")

    # Q5) Sum of natural numbers
# s = 0
# n = int(input("Tell your number where you want your sum : "))

# for i in range(1,n+1):
#     s = s + i
# print(s)

    # Q6) factorial of a number
# f = 1
# n = int(input("Tell your number for its factorial : "))
# for i in range(1,n+1):
#     f = f * i
# print(f"{n} factorial is {f}")

    # Q7) print sum of all even odd numbers in a range saparately
# n = int(input("Enter a number : "))

# oddsum = 0
# evensum = 0

# for i in range(1,n+1):
#     if i % 2 == 0:
#         evensum = evensum + i
#     else :
#         oddsum = oddsum + i

# print(f"Your even sum is {evensum} and your odd sum is {oddsum}.")

    # Q8) print factors of a number (factors : who divisible 1, and the numbers that divisible other numbers and its own number at the end.
    # prime number : which has 2 numbers only first is 1 and last is itw own number
    # composite number : divisible for all the other numbers.)
# n = int(input("Enter a number : "))
# for i in range(1,n+1):
#     if n % i == 0:
#         print(i)
        
    # Q9) print a perfect number
# n = int(input("Enter a number : "))
# s = 0

# for i in range(1,n):
#     if n % i == 0:
#         s = s + i
    
# if s == n:
#     print(f"{n} It is a perfect number ")
# else : 
#     print(f"{n} is not a perfect number")
    
    # Q10) print prime numbers
# n = int(input("Enter a number : "))
# count = 0

# for i in range(1, n+1):
#     if n %2 == 0:
#         count = count + 1

# if count == 2 :
#     print("It is the prime number")
# else :
#     print("It is the composite number")
    
    # Q11) Reverse a string without using built in function
    # String slicing a = "python" --> print(a[::-1]) --> reverse the string
# a = "python"
# rev = ""

# for i in range(len(a)-1,-1,-1):
#     rev = rev + a[i]
# print(rev)

    # Q12) Check if the string is pallindrome
# a = input("Tell your string : " )
# rev = ""

# for i in range(len(a)-1,-1,-1):
#     rev = rev + a[i]

# if rev == a:
#     print("it is a pallindrome number")
# else : 
#     print("it is not a pallindrome number")

    # Q13) Count letters , digit and special symbols in a string
# a = "P@#yn26at^&i6ve"

# char = 0
# spchar = 0
# digits = 0

# for i in a :
#     if i.isdigit():
#         digits = digits + 1
#     elif i.isalpha():
#         char = char + 1
#     else :
#         spchar = spchar + 1

# print(f"Characters {char}, Special characters {spchar}, Digits {digits}")
    # by using ascii code : 
# a = "P@#yn26at^&i6ve"

# char = 0
# spchar = 0
# digits = 0

# for i in a :
#     if (ord(i) >= 65 and ord(i) <=90) or (ord(i) >= 97 and ord(i) <=122):
#         char += 1
#     elif ord(i) >= 48 and ord(i) <= 90:
#         digits += 1
#     else :
#         spchar = spchar + 1

# print(f"Characters {char}, Special characters {spchar}, Digits {digits}")


# ascii(ord()) values of digits & alphabets
# digits from 0 to 9 --> 48 - 57
# alphabetsfrom A to Z -- > 65 - 90
# alphabetsfrom a to z -- > 97 - 122

# print(ord("9"))

# fibonacci series 
# n = int(input("Enter a term for its fibonacci series : "))
# a = 0
# b = 1

# print("Fibonacci Series : ")

# for i in range(n):
#     print(a, end=" ")
#     c = a + b
#     a = b 
#     b = c

# __________________________________________________________________________________________________________________

#  while loop

# a = 1
# while a != 20:
#     print(a)
#     a = a + 1

    # Q1) Separate each digit of a number and print on a new line
# a = int(input("please tell your number : "))

# while a > 0:
#     print(a%10)
#     a = a // 10


    # Q2) Accept a number and print its reverse
# a = int(input("please tell your number : "))

# rev = 0

# while a > 0:
#     rev = rev * 10 + a % 10
#     a = a // 10

# print(rev)

    # Q3) Check if a number is pallindrome (equal tpo its reverse)
# a = int(input("please tell a number : "))
# copy = a
# rev = 0

# while a > 0:
#     rev = rev * 10 + a % 10
#     a = a // 10
    
# if rev == copy:
#     print("It is a pallindrome number")
# else:
#     print("It is not a pallindrome number")
