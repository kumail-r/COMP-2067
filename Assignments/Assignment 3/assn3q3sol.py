fibs = [0,1] # initialize with first two numbers from the definition of the fibonacci sequence
for i in range(1,19): # iterate through the next 18 values to be added
    fibs.append(fibs[i] + fibs[i-1])  # for each one, it is the sum of the previous two entries
print('The first 20 Fibonacci numbers are: ', fibs) # print out the completed list of fibonacci values as stored in the list fibs