myList = ['apple', 'orange', 'pear', 'blueberry', 'peach']
length = len(myList)
shifted_list = [None] * length

for index in range(length):
      new_index= (index+3)%length
      shifted_list[new_index]= myList[index]

print(shifted_list)