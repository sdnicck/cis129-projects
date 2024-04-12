#!/usr/bin/env python
# coding: utf-8

# In[107]:


#Satya Dulam
#lab 8
#4/10/24

#def main():
    
def is_palidrome():
    
    # definition to compare the forward and reverse of the word
    def list_compare(wordList, reverseList):
        if (wordList == reverseList):
            return 'They match! That word is a palindrome!'
        else:
            return 'They don\'t match! That word is not a palindrome!'
        
    #user enters a word
    word = getInput('Enter a word: ')
    
    #creating lists for forward and verse 
    reverseList = []
    
    stackList = []
    
    wordList = []
    
    #turning word into a list of letters and characters
    stackList = list(word.upper())
    
    wordList = list(word.upper())
    
    #reversed list of word
    for i in range(len(stackList)):
        reverseList.append(stackList.pop())
        
    print("the word written in a forward list:",wordList)
    print("the word written in a reverse list:",reverseList)
    
    
    #prinited comparison of letters in word against reversed word        
    print(list_compare(wordList,reverseList))
    
    #print(reverse_list[0])
        
def getInput(message):
    userInput = input(message)
    while userInput == "":
        print("Please enter a word:")
        userInput = input(message)
    return userInput
    
is_palidrome()
    


# In[ ]:





# In[ ]:




