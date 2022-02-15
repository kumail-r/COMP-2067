myint = int(input('Enter a positive integer between 20 and 50: ')) # get a value from the user for myint

if myint < 20: # if myint is less than 20
    print(myint, ' is less than the minimum acceptable value.') # print out message saying myint is too small
elif myint > 50: # if myint is greater than 50
    print(myint, ' is higher than the maximum acceptable value') # print out message saying that myint is too large
else: # if myint is within accecptable range (50 >= myint >= 20)
    print(myint, ' is within the acceptable range.') # print out that myint is within acceptable range
    result = pow(myint, 3) / 7.351 # store the result of (myint^3)/7.351
    print('result = ', result) # print the value of result
    
    result2 = int(result) # store the integer value of result into result2
    print('result2 = ', result2) # print the value stored in result2

remainder = myint % 5 # calculate the remainder of dividing myint by 5 and store it into remainder
print('The remainder obtained after dividing ',myint, ' by 5 = ', remainder) # print out the value of remainder