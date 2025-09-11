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

# ==============================
# Part 1: Draw a Diamond
# ==============================
def draw_diamond():
    """
    Ask the user for an odd number for the diamond height
    and print a symmetric diamond of that height.
    """
    
    print("you have some work todo!, draw_diamond")

    # TODO: Prompt user for an odd number
    txt="Input an odd number"
    while True:
        try:
            num=int(input(txt))
            if num%2==0:
                txt="that's an even number"
                continue
            break #allow to stop the loop when the user inputs an odd number
        except ValueError:
            txt="invalid input. Try again!"


    # TODO: Draw the top half of the diamond
    for star in range (1, num+1): #+1 to include num
        if star%2==0:
            continue #skip the even numbers because only need odd number of stars
        spaces = (num - star) // 2 #number of spaces needed to center the star and floor division ensures it's not a float
        print((" " * spaces) + ("*" * star))

    # TODO: Draw the bottom half of the diamond
    for star in range(num - 1, 0, -1): #start with num-1 because there is only 1 row with num amount of stars (the widest part of the diamond), which is already executed by the top half of the diamond
        if star % 2 == 0:   # skip evens
         continue
        spaces = (num - star) // 2
        print(" " * spaces + "*" * star)
# Uncomment to test Part 1
draw_diamond()


# ==============================
# Part 2: Count Letters, Words, and Sentences
# ==============================
def text_analysis():
    """
    Ask the user for a block of text.
    Count and display:
        - Number of letters (only count a-zA-Z)
        - Number of words   (use split())
        - Number of sentences (., ?, !) 
    """

    print("you have some work todo!, text_analysis")

    # TODO: Get user input
    text = input("Enter some text: ")

    # TODO: Count letters
    letters = 0
    for ch in text:
        if not ch.isalpha():#skip non-letters
            continue
        letters=letters+1

    # TODO: Count words
    words = 0
    for word in text.split():#breaks the string from the spaces
        words = words + 1

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
    Ask the user for text and a shift value.
    Provide options to encrypt or decrypt the text using a Caesar cipher.
    """

    print("you have some work todo!, caesar_cypher")

    # TODO: Get user input text
    text = input("Enter text: ")

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
              new_code = ord(ch) + shift
              if new_code > ord('Z'): #if once we shift the letters and it goes over Z then it wraps back around the alphabet
                    new_code = new_code - 26
              elif new_code < ord('A'): 
                    new_code = new_code + 26
              result = result + chr(new_code)
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