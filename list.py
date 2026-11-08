    #  List 
# ordered nature you can access any element at any point of time.
# mutable in nature but most important thing is that the string is immutable i.e it cannot change the string value.
# you can have duplicat values l = [1,1,2,2,3,3,4,4,].
# you can add anything in list int numbers, float, string, boolean, values, print().


# a = [12,23,34,45,56,67]
# print(a)
# print(type(a))
# print(a[1])
# print(a[-1])

# l = [10,22,30,40,50]
# l[1] = 20
# print(l)


    # TRAVERSING ON A LIST
# a = [10,20,30,40,50]

# without traversing 
# print(a)

# with traversing using loop method-I : Traversing on values
# for i in a:
#     print(i)

# with traversing using loop method-II : Traversing on index (as well as it works on both index and values at same time )
# for i in range(0,len(a)):
#     print(f"{i} : {a[i]}")

    # METHODS 

# print(dir(list)) 
# code to check all the methods are used for list 
# the list methods are as follows : 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

# a = [10,75,20,88,40,55,90]
# a.append(60,) #add values at the last 
# a.insert(2,30) #add values where you want
# a.pop() #removes the last value "[-1]" 
# a.remove(55) #we have to provide the actual value to remove 
# a.clear() #clear all values the list is totally empty
# a.sort() #assending order and returns none
# a.sort(reverse=True) #when u do this it provide desending order and returns none
# a.extend()
# a.index()
# a.count()
# print(a)

    # EXERCISES
    
# Q1) Print all positive and negative elements separately.

# l = [3,-1,4,-5,9]

# pos = []
# neg = []

# for i in l:
#     if i >= 0:
#         pos.append(i)
#     else :
#         neg.append(i)
# print(f"Your positive elements are {pos}")
# print(f"Your negative elements are {neg}")


# Q2) Find the mean (average) of all list elements.

# l = [10, 20, 30, 40]

# sum = 0

# for i in l:
#     sum += i
# avg = sum / len(l)
# print(f"Your average of element is {avg}")


# Q3) Find the greatest element and print its index.

# l = [4, 8, 2, 9, 1]

# largest = l[0]
# index = 0

# for i in range(0,len(l)):
#     if l[i] > largest:
#         largest = l[i]
#         index = i 
# print(f"You largest element is {largest} at index {index}")


# Q4) Find the second greatest element.

# l = [4, 7, 2, 9, 1 , 8]

# largest = l[0]
# second_largest = l[0]

# for i in l:
#     if i > largest:
#         second_largest = largest
#         largest = i
#     elif i > second_largest:
#         largest = i
# print(f"You second largest element is {largest}")


# Q5) Check if the list is already sorted.

# l = [3, 1, 4]
# for i in range(len(l)-1):
#     if l[i] > l[i+1]:
#         print("Your list in not sorted")
#         break
# else :
#     print("your list is sorted")





        # EXERCISES 

    # Level 1 – Beginner solutions
    
# Q1. Find the sum of all elements
# a = [10,20,30,40,50]
# total = 0 

# for i in a:
#     total += i
# print(f"Total sum of element are : {total}")


# Q2. Count even and odd numbers
# a = [10, 15, 20, 25, 30, 35]

# even = 0
# odd = 0

# for i in a :
#     if i %2 == 0:
#         even += 1
#     else :
#         odd += 1
# print(f"Count of Even numbers : {even}")
# print(f"Count of Even numbers : {odd}")

# Q3. Find the smallest element
# a = [10, 5, 30, 2, 50]

# smallest = a[0]

# for i in a :
#     if i < smallest:
#         smallest = i
# print(f"Smalles number from given element is : {smallest}")

# Q4. Count positive, negative and zero values
# a = [10, -5, 0, 20, -10, 0]
# pos = 0
# neg = 0
# zero = 0

# for i in a :
#     if i > 0 :
#         pos += i
#     elif i < 0:
#         neg += i
#     else :
#         zero += i
# print(f"Positive numbers count are : {pos}")
# print(f"Negative numbers count are : {neg}")
# print(f"Zero number count : {zero}")


# Q5. Reverse a list without using reverse()
# a = [10, 20, 30, 40, 50]
# rev = []

# for i in range(len(a)-1,-1,-1):
#     rev.append(a[i])
# print(rev)



# Q6. Search for an element in a list
# a = [10, 20, 30, 40, 50]

# search = int(input("Enter a element to search : "))
# for i in range(len(a)):
#     if a[i] == search:
#         print(f"Element found at index", i)
#         break
#     else :
#         print("Not found")

# Q7. Count how many times a number appears
# my method 
# a = [1, 2, 2, 3, 3, 3, 4]
# count = 0

# for i in range(len(a)):
#     if i == a[i]:
#         count += i
#         print(f"count of same number is {count}")
#         break

# chatgpt method 
# a = [1, 2, 2, 3, 3, 3, 4]
# for i in range(len(a)):
#     if a[i] not in a[:i]:
#         print(a[i], "appears" , a.count(a[i]), "times")

# a = [1, 2, 2, 3, 3, 3, 4]

# print(a[:0]) 
# print(a[:1])
# print(a[:2])
# print(a[:3])
# print(a[:8])

# Q8. Copy one list into another
# a = [10, 20, 30, 40]
# b = []

# for i in a :
#     b.append(i)
# print(f"Original {a}")
# print(f"Copied {b}")


# Q9. Remove all duplicate elements
# a = [1, 2, 2, 3, 3, 4, 4, 5]
# b = []
# for i in a:
#     if i not in b:
#         b.append(i)
# print(b)


# Q10. Find the length without using len()
# a = [10, 20, 30, 40, 50]
# count = 0

# for i in a:
#     count += 1
# print(f"lentgh {count}")