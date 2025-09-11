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