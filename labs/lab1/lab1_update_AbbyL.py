# ==============================
# Main Program
# ==============================
def main():
    while True:
        print("Lab 1 - Python Basics")
        print("1. Draw Diamond")
        print("2. Text Analysis")
        print("3. Caesar Cipher")
        choice = input("Select part to run (1-3): ")
        
        if choice == "1":
            draw_diamond()
        elif choice == "2":
            text_analysis()
        elif choice == "3":
            caesar_cipher()
        else:
            exit()



"""
Lab 1 - Python Basics
Author: Abby Liem
Instructions: Complete each part below. Save your work and commit + sync in Codespaces.
"""

'''
Abby, you did a great job on this lab! Grade A-.
Be more consistant with your use of spaces.  I've edited
your style a little below but haven't changed any code.

Your Caesar cipher is a little weak.  What happens if a user
enters a shift of 60?  see comments below
'''

# ==============================
# Part 1: Draw a Diamond
# ==============================
def draw_diamond():
    """
    This is to draw a diamond that is not filled.
    To do this, each row is made up of:
      - Spaces before the first star, which decrease by 1 each row as we go down.
      - Spaces between the two stars (inner spaces), which increase by 2 each row as we go down.
    After that, the bottom half repeats the same pattern in reverse to close the diamond.
    We use a loop to repeat this pattern:
      - figure out how many front spaces to add
      - print the first star
      - add the inner spaces
      - and then print the second star
    """
    
    print("you have some work todo!, draw_diamond ")

    # TODO: Prompt user for an odd number
    txt = "Input an odd number"    
    while True:
        try:
            num = int(input(txt))
            if num % 2 == 0:
                txt = "that's an even number "
                continue
            break #allow to stop the loop when the user inputs an odd number
        except ValueError:
            txt = "invalid input. Try again! "


    # TODO: Draw the top half of the diamond
    mid = num // 2
    for i in range(mid + 1): #+1 to include the middle row also
        spaces = " " * (mid - i) #front spaces is one less after each row
        if i == 0:
            print(spaces + "*")
        else:
            inner_spaces = " " * (2 * i - 1) #inner spaces are 0, 1, 3, etc. So it increases by 2 * the row. But then this would get 0, 2, 4, so we need to minus one.
            print(spaces + "*" + inner_spaces + "*")

    # TODO: Draw the bottom half of the diamond
    for i in range(mid - 1, -1, -1): #the exact same as the top half, but we start with mid-1 because we already did the widest row of the diamond on top
                                     # the middle -1 is stop, meaning to make sure the last is 0
                                     # the last -1 is the step, which means just to go backwards
        spaces = " " * (mid - i)
        if i == 0:
            print(spaces + "*")  # just one star
        else:
            inner_spaces = " " * (2 * i - 1)
            print(spaces + "*" + inner_spaces + "*")
# Uncomment to test Part 1
draw_diamond()


# ==============================
# Part 2: Count Letters, Words, and Sentences
# ==============================
def text_analysis():
    """
    This function asks the user to enter some text and it will:
      - Count how many letters are in the text (skipping spaces, numbers, and punctuation).
      - Count how many words there are by splitting the text at spaces.
      - Count how many sentences there are by checking for '.', '!', or '?'.
    To do this, we use loops to go through the text character by character or word by word,
    add up the counts, and finally print out the results.
    """

    print("you have some work todo!, text_analysis")

    # TODO: Get user input
    text = input("Enter some text: ")

    # TODO: Count letters
    letters = 0
    for ch in text:
        if not ch.isalpha():#skip non-letters
            continue
        letters = letters + 1

        '''
        you could change the above to:
        if ch.isalpha(): letters += 1
        '''

    # TODO: Count words
    words = 0
    for word in text.split():#breaks the string from the spaces
        words = words + 1

    '''
    you could change the above to:

    word_list = text.split()
    words = len
    '''

    # TODO: Count sentences
    sentences = 0
    for ch in text:
        if ch =="." or ch=="!" or ch=="?":  
            sentences = sentences + 1

    # TODO: Print the results
    print(f"Letters: {letters}")
    print(f"Words: {words}")        # replace 0
    print(f"Sentences: {sentences}")    # replace 0

# Uncomment to test Part 2
text_analysis()


# ==============================
# Part 3: Caesar Cipher – Encrypt and Decrypt
# ==============================
def caesar_cipher():
    """
    This function is to decrypt or encrypt a text.
    - First, we prompt to get the input text, the shift value (how many letters to move),
      and the choice (encrypt or decrypt).
    - If decrypting, we flip the shift to negative so the letters move backwards.
    - Then we go through each character in the text by using a for loop:
        - If it's a letter, we use ord() to change the letter into a number according to the alphabet so we can then add or subtract the shift value. If it’s not a letter (like a space or punctuation), we just keep it the same.
        - But we want to make sure the letter wraps around the alphabet to make sure there are no errors and that it won't return non-alphabetical characters (so after Z it becomes A instead of '{').
        - Then use chr() to change the number back into a letter.
        - To make sure that we keep the capitalization the uppercase and lowercase letters are handled separately.
    """

    print("you have some work todo!, caesar_cypher")

    # TODO: Get user input text
    text = input("Enter text: ")


    '''
    your shift value should be entered in a while true block.  also check that a int
    between 1 and 25 is entered
    '''
    # TODO: Get shift value
    shift = int(input("Enter shift value (integer): "))   

    # TODO: Ask user whether to encrypt or decrypt
    choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()


    # TODO: Implement encryption and decryption logic
    if choice=="d":
        shift=-shift #shift is normally positive (shift alphabet forward which is to encrypt), so need to move backwards to decrypt

    result = ""
    for ch in text:
        if ch.isalpha(): #to only change the letters
            if ch.isupper(): #to make sure letters stay uppercase or lowercase
              
              #############let's examine this block################
              new_code = ord(ch) + shift
              if new_code > ord('Z'): #if once we shift the letters and it goes over Z then it wraps back around the alphabet
                    new_code = new_code - 26
              elif new_code < ord('A'): 
                    new_code = new_code + 26
              result = result + chr(new_code) #chr turns the number back into a letter
              #####################################################

              '''
              this will work if your shift value is between 1 and 25
              we can clean this up by 0 basing the ascii table so 65
              becomes 0 for the letter A, and then using % operator
              and then adding back ord('A') to get ascii table value

              new_code = (ord(ch) - ord('A') + shift) % 26 + ord('A')
              result = result + chr(new_code)

              for eample, suppose we need to shift the letter 'A'
              (ord(ch) - ord('A') + shift) = shift
              because in this case ch = 'A'

              regardless of what shift is:
              (ord(ch) - ord('A') + shift) % 26 will produce a value
              between 1 and 25 and adding back ord('A') gets me the 
              correct ascii table value for the shift.
              '''



            else:
                # lowercase letters
                new_code = ord(ch) + shift
                if new_code > ord('z'):
                    new_code = new_code - 26
                elif new_code < ord('a'):
                    new_code = new_code + 26
                result = result + chr(new_code)
        else:
            result += ch   # keep spaces/punctuation

   

    # TODO: Print the final result
    print("Result:", result)

# Uncomment to test Part 3
caesar_cipher()




if __name__ == "__main__":
    main()