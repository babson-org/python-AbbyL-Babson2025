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
            continue #skip the even numbers
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