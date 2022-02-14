name = str(input('Enter your name: ')) # ask for first name
vowels = ['a', 'e', 'i', 'o', 'u'] # list containing all vowels
if name[0].lower() in vowels: # check if the first character in name is in vowels
    print('Your name starts with a vowel.') # print this out if it matches with a letter in vowels
else:
    print('Your name starts with a consonant.') # print this outt if it does not match with a letter in vowels
print('The first letter of your name is: ', name[0].upper()) # print out the first letter in the name capitalized