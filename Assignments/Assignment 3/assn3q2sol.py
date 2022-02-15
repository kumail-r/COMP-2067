total = 0 # initialize total
while total <= 100: # while loop will continue to loop until the condition of total being less than or equal to 100 is no longer true
    num = float(input('Please enter a number: ')) # ask user for input
    total = total + num # the new total is equal to the old total plus the new input value
x = pow(total,2) # x = total^2
print('The square of ', total, ' is ', round(x,1)) # print out the values of total and the value of x rounded to one decimal point