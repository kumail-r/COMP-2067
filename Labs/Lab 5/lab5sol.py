x = int(input('Enter an integer between 0 and 8: ')) # get an input value from the user
count = 0 # count starts at 0 before entering the loop
while x < 50: # loop will keep re-looping unless x is greater than 50
    count += 1 # count goes up by one every time the loop restarts
    print('x = ', x) # print out the current value of x
    if x % 9 == 0: # if the remainder of dividing x by 9 is 0, x must be a multiple of 9
        print('found multiple of 9') # print out saying that a multiple of 9 was found
        break # break the loop
    x = x + 10 # add 10 to x
print('The final value of x is ', x) # print out the final value of x
print('The loop was entered ', count, ' times.') # print out the value in count, which will display the number of times the loop was entered
