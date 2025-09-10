from classes.week00.second_class.utils import clear_screen
'''
# 1

Write down the steps a program would need to make a cup of tea. Then implement a Python 
function make_tea() that prints each step.
'''
# enter your code here
def make_tea():
    steps = [
        "1. Boil water.",
        "2. Place a tea bag into a cup.",
        "3. Pour the hot water into the cup.",
        "4. Let the tea steep for a few minutes.",
        "5. Remove the tea bag.",
    ]
    
    for step in steps:
        print(step)

pause=input('pause')
clear_screen()
'''
#2

Given a list [2, 4, 6, 8, 10], write a program that prints the next three numbers in the list.  
(the ones after 10)
'''
# enter your code here
list=[2, 4, 6, 8, 10]
x=10
for i in range(3):
    x=x+2
    list.append(x)

print(list)


pause=input('pause')
clear_screen()
'''
#3

Write a program that asks the user for their first and last name, then prints a greeting:
"Hello, <first name> <last name>!"
'''
# enter your code here
first= input("Enter your first name")
last= input("Enter your last name")
print(f"Hello, {first} {last}")

pause=input('pause')
clear_screen()
'''
#4

Write a program that prints your Python version and platform using the sys and platform modules.
'''
# enter your code here
import sys
import platform
import pprint
pprint.pprint(dir(sys))

pause=input('pause')
clear_screen()
'''
#5

Ask the user to input two numbers. Calculate and print their sum, difference, product, 
and division (both / and //).
'''
# enter your code here
first= int(input("Enter a number"))
second= int(input("Enter a second number"))

print("sum=",(first+second))
print("difference=",(first-second))
print("product=",(first*second))
print("division=",(first/second))
print("floor division=", (first//second))

pause=input('pause')
clear_screen()
'''
#6

Ask the user to input a sentence. Print it in uppercase, lowercase, with the first letter 
capitalized, and split it into words.
'''

# enter your code here
sentence = input("Enter a sentence: ")

# Print in different formats
print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())
print("Capitalized:", sentence.capitalize())
print("Words:", sentence.split())


pause=input('pause')
clear_screen()
'''
#7

Calculate the result of the following without parentheses and then with parentheses:
10 + 2 * 5 / 2 - 3 ** 2
'''
# enter your code here
print(10 + 2 * 5 / 2 - 3 ** 2)
print((10 + 2) * 5 / 2 - 3 ** 2)

pause=input('pause')
clear_screen()
'''
#8

Create a list of your three favorite foods. Replace the second item with a new one, 
then print the list.
'''
# enter your code here
food=["sushi", "indomie", "pasta"]
food[1]="ramen"
print(food)



pause=input('pause')
clear_screen()
'''
#9

Create a tuple with four numbers. Try to change the first number (observe the error) 
and then print the tuple.
'''
# enter your code here
tuple=(1,2,3,4)
tuple[0]=2
print(tuple)

pause=input('pause')
clear_screen()
'''
#10

Create a dictionary representing a student (name, age). Update the age. Create a list of 
favorite numbers and add a new number.
'''
# enter your code here
student = {
    "name": "Abby",
    "age": 21
}
student["age"]=22

numbers=[1,2,3]
numbers.append(4)
print(numbers)

pause=input('pause')
clear_screen()
'''
#11

Ask the user to input their favorite quote. Save it to a file quotes.txt 
and read it back to print it.
'''
# enter your code here
quote=input("Enter your favorite quote")
with open("quotes.txt") as file:
    text = file.read()
    print(text)

pause=input('pause')
clear_screen()
'''
#12
Ask the user to input 5 numbers (one at a time), store them in a list, and print the sum and average.
'''
# enter your code here
first=int(input("Enter the first number"))
second=int(input("Enter the second number"))
third=int(input("Enter the third number"))
fourth=int(input("Enter the fourth number"))
fifth=int(input("Enter the fifth number"))

list=[first,second,third,fourth,fifth]
sum= sum(list)
average=sum/len(list)

print(sum)
print(average)

pause=input('pause')
clear_screen()