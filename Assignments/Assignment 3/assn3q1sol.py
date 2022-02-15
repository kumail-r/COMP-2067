wordlist = ['hat', 'book', 'house', 'flower', 'tree', 'grass', 'cheetah', 'lion', 'tiger', 'car', 'boat'] # initialize list of words
vowels = ['a', 'e', 'i', 'o', 'u'] # a list of all the vowels in the english language

for i in range(0,len(wordlist), 3): # starting at 0 iterate by 3 until the end of the list
    vowelcount = 0 # initialize the word's vowel count (it resets here for every word)
    for j in wordlist[i].lower(): # iterate through each letter in the word
        if j in vowels: # if the letter is a vowel (by checking if it is present in the vowels list that was previously declared)
            vowelcount = vowelcount + 1 # add 1 to the vowel count variable
    print(wordlist[i], 'contains ', vowelcount, ' vowel(s)') # print out the number of vowels in the word

    if vowelcount >= 3: # if the vowelcount ends up as 3 or higher
        print('***Found string with 3 or more vowels!***') # print out a message declaring that the vowelcount is 3 or higher
        break # break the loop if the vowelcount is 3 or higher