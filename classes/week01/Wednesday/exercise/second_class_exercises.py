#%%
# print 'hello' 5 times using an arithmetic operator
x='hello'
print(x*5)

#%%
# print 'hello' 5 times using a loop
time = 0
while time<5:
      print('hello')
      time=time+1

#%%
# print 'hello' 5 times on the same line using a loop
time = 0
while time<5:
      print('hello', end='')
      time=time+1

#%%
''' using nested loops print the following:

00 01 02
10 11 12
20 21 22

'''
for row in range(3):
      for col in range(3):
            print(str(row)+str(col), end=' ')
      print()
print()      
#%%
# define txt and input some text from the keyboard into it
txt=input("Please enter a text: ")

#%%
# print each letter in txt 
for let in txt:
      print(let)

#%%
# assign the variable letter to the first letter in txt
letter=txt[0]

#%%
# print out all the letters in txt that are equal to the first letter
for let in txt:
      if let==letter:
            print(let, end='')
'''
say txt = 'the cat in the hat was read today'
't' is the first letter

result: tttt
'''

#%%
myList = ['apple', 'orange', 'pear', 'blueberry', 'peach']
length = len(myList)
shifted_list = [None] * length

for index in range(length):
      new_index= (index+3)%length
      shifted_list[new_index]= myList[index]

print(shifted_list)
      
'''
# suppose we had a list of n elements. create a new list that
  shifts the elements by 3

    myList = ['apple', 'orange', 'pear', 'blueberry', 'peach']
      shifted_list = ['pear', 'blueberry', 'peach', 'apple', 'orange']

        Hints:
             1) use len(), % (used to keep in range), enumerate (enumerate= loop through sequence)
                  2) also assign shifted_list = [None] * length  (you'll need to determine 
                          the length variable)
                               3) shift inside the for loop
                                    4) print out the printed list outside the for loop
                                    '''



                                    # %%
                                    