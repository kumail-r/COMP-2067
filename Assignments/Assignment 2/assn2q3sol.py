L1 = [5, -34, 0, 98, -11, 244, 193, 28, -10, -20, 45, 67] # initialize L1 as a list of 10 integers
print('L1 = ', L1) # print out L1
x = int(input("Enter an integer x in the range 0 to " + str(len(L1) - 1) + ": ")) # ask the user for an input between 0 and n-1 and store the value in x

if (x >= 0) and (x <= len(L1) - 1): # check if x is within n-1 >= x >= 0
    print('The x_th element of L1 is: ', L1[x]) # print out x_th element of L1
    if x in L1: # check if x is present within the elements of L1
        print(x, ' occurs in L1 at the position: ', L1.index(x)) # if it is present, print out the index it occurs at
    else: # x is not present among the elements of L1
        print(x, ' does not occur in L1.') # print out that it does not occur within L1
    
    if (x % 2 == 0) and x > 0: # check if x is even (even numbers divided by 2 have a remainder of 0) and greater than 0
        print('The first ', x, ' elements of L1 are: ', L1[:x]) # prints out the first x elements from L1
    elif(x % 2 == 1) and x > 0: # check if x is odd (odd numbers divided by 2 have a remainder of 1) and greater than 0
        print('The last ', x, ' elements of L1 are: ', L1[(len(L1) - x):]) # prints ouf the last x elements from L1
    else: # the only possible non-negative integer that can end up here is 0
        print([]) # print out an empty list
else: # x is outside of n-1 >= x >= 0 
    print('You did not enter a valid input!') # print out message saying x is invalid