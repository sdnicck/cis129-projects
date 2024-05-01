#!/usr/bin/env python
# coding: utf-8

# In[16]:


#Satya Dulam
#4/30/24
#mod 10 lab

def main():
    
    #collecting amount from user
    dollarAmount = getFloat("Please input a dollar amount up to one cent:")

    #converting input into a str with commas, a formated to the correct decimal point 
    check = str(f'[{dollarAmount:*>10,.2f}]')
    
    #printing the input that is formated correctly
    print('\n\n$...',check)

# user input validation to only let the user enter a number
def getFloat(message):
    while True:
        try:
            dollarAmount = float(input(message))
            return dollarAmount
        except ValueError:
             print("\nIncorrect data entered, please re-attempt")
    
main()




