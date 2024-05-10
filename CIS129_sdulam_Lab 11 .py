#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Satya Dulam
#CIS129
#mod 11 Lab
#5/7/24

#main function
def main():
    
    #constants used to bound user
    LOW = 0
    HIGH = 100
    
    #open new text file (question 9.1)
    with open('grades-test.txt', mode = 'w') as grades:
        #setting variables to zero
        keepGoing = 'y'
        counter = 0
        #priming the user to enter data
        while keepGoing == 'y':
            counter = counter + 1
            studentName = input('Enter the first name of the student: \n')

            studentGrade = getValidNum('Enter the student\'s grade: \n',LOW,HIGH)
            
            #setting data according to user input
            if studentGrade >= 90:
                letterGrade = 'A'
            elif studentGrade >= 80 and studentGrade <90:
                letterGrade = 'B'
            elif studentGrade >=70 and studentGrade <80:
                letterGrade = 'C'
            elif studentGrade >=60 and studentGrade <70:
                letterGrade = 'D'
            else:
                letterGrade = 'F'
                
            #adding all the necessary data int

            inputInfo = str(counter) + " " + studentName.title() + " " + str(studentGrade) + " "+ letterGrade + "\n" 

            keepGoing = input("Would you like to enter more grades? (enter y if yes): ")
            
            grades.write(inputInfo)

    total = 0
# reading the txt file with individual grades and total (question 9.2)
    with open('grades-test.txt', mode='r') as grades:
        print('\n' + f'{"Student Number":<20}{"Name":<10}{"Score":>10}{"Grade":>10}')
        for record in grades:
            number, name, grade, letter = record.split()    
            print(f'{number:<20}{name:<10}{grade:>10}{letter:>10}')
            
            final = int(grade)
            total += final
            
            average = total/counter
        print('\n Average for Class:', f'{average}')
    
                
            
def getInteger(message):
    while True:
        try:
            userInput = int(input(message))
            return userInput
        except ValueError:
            print("Incorrect data entered, please re-attempt")
        
def getValidNum(message, LOW, HIGH):
    newValue = getInteger(message)
    #validates the user's input using isInvalid() to check conditions
    while isInvalid(newValue, LOW, HIGH):
        print("Invalid number! Please enter a number within the valid range of the section")
        newValue = getInteger(message)
    return newValue

#isInvalid is called in the getValidNum() functioin
def isInvalid(newValue, LOW, HIGH):
    #returns True if value is invalid (bad data)
    #returns False if value is valid (good data)
    #many conditions can be added to this function
    if newValue < LOW:
        return True #invalid data, too low
    if newValue > HIGH:
        return True #invalid data, too high 
    return False #passed all checks, good data

main()



# In[2]:


import csv

def main():

    with open('grades.csv','w',newline='') as grades:
        writer = csv.writer(grades)
        keepGoing = 'y'
        counter = 0
        #priming the user to enter data
        while keepGoing == 'y' and counter >3:
            firstName = input('Enter the first name of the student: \n')
                
            lastName = input('Enter the last name of the student: \n')
            
            counter = counter +1 
            studentGrade = getValidNum('Enter the student\'s grade: \n',LOW,HIGH)

            #adding all the necessary data int

            inputInfo = str(counter) + " " + studentName.title() + " " + str(studentGrade) + " "+ letterGrade 

            keepGoing = input("Would you like to enter more grades? (enter y if yes): ")

        writer.writerow(inputInfo)

    total = 0
    # reading the txt file with individual grades and total (question 9.2)
    with open('grades-test.txt', mode='r') as grades:
        print('\n' + f'{"Student Number":<20}{"Name":<10}{"Score":>10}{"Grade":>10}')
        for record in grades:
            number, name, grade, letter = record.split()    
            print(f'{number:<20}{name:<10}{grade:>10}{letter:>10}')

            final = int(grade)
            total += final

            average = total/counter
        print('\n Average for Class:', f'{average}')
    
            
def getInteger(message):
    while True:
        try:
            userInput = int(input(message))
            return userInput
        except ValueError:
            print("Incorrect data entered, please re-attempt")
        
def getValidNum(message, LOW, HIGH):
    newValue = getInteger(message)
    #validates the user's input using isInvalid() to check conditions
    while isInvalid(newValue, LOW, HIGH):
        print("Invalid number! Please enter a number within the valid range of the section")
        newValue = getInteger(message)
    return newValue

#isInvalid is called in the getValidNum() functioin
def isInvalid(newValue, LOW, HIGH):
    #returns True if value is invalid (bad data)
    #returns False if value is valid (good data)
    #many conditions can be added to this function
    if newValue < LOW:
        return True #invalid data, too low
    if newValue > HIGH:
        return True #invalid data, too high 
    return False #passed all checks, good data

main()


# In[ ]:




