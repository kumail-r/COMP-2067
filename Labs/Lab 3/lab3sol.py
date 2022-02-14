list1 = ['windsor', 'toronto', 'ottawa', 'montreal', 'vancouver'] # initialize list1
print("list1 = ", list1) # print out list1

print("The last 3 characters of the first element of list1 are: ", list1[0][4:]) # print out the last 3 characters of the first element in list1

cityname = str(input("Enter the name of a city in lowercase: ")) # ask a user for the name of a city (must be lowercase)
print("cityname = ", cityname.upper()) # print out capitalized city name

list1.append(cityname) # append cityname to the end of list1
print("The updated list1 after appending item is: ", list1) # print out the updated list1

print("The minimum value in list1: ", min(list1)) # print out minimum value in list1
list1[list1.index(min(list1))] = 'minval' # replace minimum value with the string 'minval' inside of list1
print('The updated list1 after replacing item is ', list1) # print out the updated list1

year = int(input("Enter your year of birth (yyyy); ")) # get user input for the year
print("year = ", year) # print out value in year

sum = year + len(list1) # number of elements in list1 + year
print("Number of elements in list1 is: ", len(list1)) # print number of elements in list1
print("sum = ", sum) # print value of sum