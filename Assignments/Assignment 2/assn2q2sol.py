digit = str(input('Enter a positive integer (digits only): ')) # ask for input and store within digit
if digit.isdigit(): # check if the provided string is a digit
    digit = int(digit) # make digit an integer since it is confirmed to be a digit
    if digit % 2 == 0: # if the remainder of dividing digit by 2 is 0, that means it is even
        print('You entered an even number') # print out reminder that digit is even
    elif digit % 7 == 0: # if the remainder of dividing digit by 7 is 0, that means that it is divisible by 7
        print('You entered an odd number that is a multiple of 7') # print out saying that it is an odd number divisible by 7 (it must be odd because the first if failed, thus it cannot be even)
    else: # if it is not even, it must be odd. It must also not be a multiple of 7
        print('You entered an odd number that is NOT a multiple of 7') # print out that it is odd and not a multiple of 7
else: # provided digit was confirmed not to be a positive integer
    print('You did not enter a valid input!') # print out that provided string was not a positive integer