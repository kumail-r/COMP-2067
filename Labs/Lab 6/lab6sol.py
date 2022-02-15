def multiply_lists(list1, list2): # define function with two inputs
    product = [] # declare empty product list
    for i in list1: # start iterating through list1
        for j in list2: # start iterating through list2
            product.append(i * j) # add the product of the two elements to the product list
    return product # return the completed product list

list1 = [4, 2, 7] # declare list1
list2 = [3, 1, 9, 2] # declare list2
print('list1 = ', list1, ' ;     list2 = ', list2) # print out the values stored in list1 and list2

prod_list = multiply_lists(list1, list2) # store the value returned by the function multiply_lists using list1 and list2 into prod_list
print('prod_list = ', prod_list) # print the values stored within prod_list

print('sum = ', sum(prod_list)) # print out the sum of all the elements in prod_list

print('Number of occurrences of 4 is: ', prod_list.count(4)) # print out the number of occurrences of 4 in prod_list using the .count() method

print('72 is in prod_list: ', 72 in prod_list) # print out whether or not 72 can be found within prod_list using the 'in' operator

prod_list.sort() # sort the list using the .sort() method
print('sorted list = ', prod_list) # print out the sorted list