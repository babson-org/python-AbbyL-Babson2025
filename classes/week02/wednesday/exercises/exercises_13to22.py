
from classes.week00.second_class.utils import clear_screen
'''
#13 - Conditional Logic
Ask the user for a number and print whether it is positive, negative, or zero.
'''
# enter code here
num= int(input("Enter a number"))

if num>0:
    print("your number is positive")
elif num<0:
    print("your number is negative")
else:
    print("your number is zero")


pause=input('pause')
clear_screen()

'''
#14 - Even/Odd Check
Ask the user for a number and print if it is even or odd.
'''
# enter code here
num=int(input("Enter a number"))

if num%2==0:
    print("your number is even")
else:
    print("your number is odd")


pause=input('pause')
clear_screen()

'''
#15 - Boolean Operators
Ask the user for two numbers and check if both are positive, either is positive, or none is positive.
'''
# enter code here
num1=int(input("Enter a number"))
num2=int(input("Enter another number"))

if num1>0 and num2>0:
    print("numbers are both positive")
elif num1>0 or num2>0:
    if num>0:
     print(num1, "is a positive number")
    else:
        print(num2, "is a positive number")
else:
    print("none of the numbers are positive")

pause=input('pause')
clear_screen()

'''
#16 - For Loop
Print all numbers from 1 to 20, skipping multiples of 3.
'''
# enter code here
for i in range(1,20):
    if i%3==0:
        continue
    print(i)


pause=input('pause')
clear_screen()

'''
#17 - While Loop
Ask the user to guess a secret number (hardcoded) until they get it right.
'''
# enter code here
x=3
text=int(input("Guess the number"))

while text!=x:
    print("try again")

print("correct")


pause=input('pause')
clear_screen()

'''
#18 - Break / Continue
Print numbers 1-10 but stop printing when you reach 7 and skip 3.
'''
# enter code here
for i in range (1,10):
    if i==3:
        continue
    print(i)
    if i==7:
        break


pause=input('pause')
clear_screen()

'''
#19 - Function Definition
Write a function square(x) that returns the square of a number and test it.
'''
# enter code here
def square(x):
    return x * x


pause=input('pause')
clear_screen()

'''
#20 - Function with Mutable Argument
Write a function add_item(lst, item) that appends item to lst and observe the effect on the original list.
'''
# enter code here
def add_item(lst,item):
   item.append(lst)
   return lst


pause=input('pause')
clear_screen()

'''
#21 - Comments / Documentation
Write a function greet(name) with single-line and multi-line comments explaining each step.
'''
# enter code here
def greet(name):
    print("Hello"+name)



pause=input('pause')
clear_screen()

'''
#22 - Combining Tools
Ask the user to enter 5 names. Store them in a list, capitalize each name, sort the list, and print it.
'''
# enter code here
list=[]
for i in range(5):
    name=input("enter a name")
    name.capitalize()
    name.append(list)
    name.sort()
    print(list)



pause=input('pause')
clear_screen()

