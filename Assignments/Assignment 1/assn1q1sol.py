books = int(input("How many books do you have?")) # prompt user for number of books (integer)
boxes = books/15 # calculate the number of boxes as a float
fullBoxes = int(boxes) # make integer, which will floor the value to the 
print("You will need ", boxes, " box(es) for your books.") # print out value stored in boxes
print("You will need ", fullBoxes, " FULL box(es) for your books.") # print out value stored in fullBoxes