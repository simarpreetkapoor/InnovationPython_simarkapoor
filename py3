

1. #Create a list of 10 elements of four different data types like int, string, complex and float.
Ans.



l = [2,3.7,"sam",8,[a+7y],9,10,"John",4.9,5]

====================================================================================


2. #Create a list of size 5 and execute the slicing structure

Ans.

My_friends = ["Sam", "Bob", "Anne", "john",7]
print(My_friends[1:3])


print(My_friends[0:2])

print(My_friends[4:5])
==============================================================================================


3. #Write a program to get the sum and multiply of all the items in a given list.

Ans.

l= [1,2,3,4,5]

print(sum(l))
# or
Sum = (l)
print(Sum)

list = [1, 2, 3, 4, 5]

result = 1
for i in list:
    result = result*i
print(result)

=============================================================================================

4. # Find the largest and smallest number from a given list.

Ans.

list = [1, 2, 3,6,22,99,100, 4, 5,]
list.sort()
print(list)
print("The smallest element is :",list[0],     "\n"
"The largest element is :", list[-1])


================================================================================================

7.#  Write a program to replace the last element in a list with another list.

Ans.
l = [1,3,5,7,9,10], [2,4,6,8]
print(l[0][0:5]+l[1])

===============================================================================================
8. # Create a new dictionary by concatenating the following two dictionaries:
Ans.

a = {1: 10, 2: 20}
b = {3: 30, 4: 40}
a.update(b)
print(a)

10.# Write a program which accepts a sequence of comma-separated numbers from console and
#generates a list and a tuple which contains every number in the form of string.

Ans.

values = input("Input some comma seprated numbers : ")
list= values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)
