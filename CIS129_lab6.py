# Satya Dulam
#CIS129
#Lab 6
#3/26/24

# Assume that hot dogs come in packages of 10, and hot dog buns come in packages of 8. Design a modular program that calculates the number of packages of hot dogs and the number of packages of hot dog buns needed for a cookout, with the minimum amount of leftovers. The program should ask the user for the number of people attending the cookout, and the number of hot dogs each person will be given. The program should display the following:

# 1. The minimum number of packages of hot dogs required.
# 2. The minimum number of packages of bunds required
# 3. The number of th hot dogs that will be left over
# 4. The number of bunds that will be left over

import math

#main module
def main(): 
    
#local variable for the total number of hot dogs needed.
    total = 0
    
#input - get the total number of hot dogs needed
    total = getTotalHotDogs()

#processing - Name constants for the package sizes
    DOGS = 10 #hot dogs in a package
    BUNS = 8 # hot dog buns in a package

#local variables
    dogsLeft = 0
    bunsLeft = 0
    minDogs = 0
    minBuns = 0

#calculate the number of left over hot dogs
    dogsLeft = (DOGS - (total % DOGS)) % DOGS
    
#calculate the minimum number of packages of hot dogs
    minDogs = math.ceil(total/DOGS)
    
#calculate the number of left over hot dog buns
    bunsLeft = (BUNS - (total % BUNS)) % BUNS
    
#calculate the minimum number of packages of hot dog buns
    minBuns = math.ceil(total/BUNS)

#Display the results
    
    showResults(minDogs, minBuns, dogsLeft, bunsLeft)

def getTotalHotDogs():
    
    #Declare local variables
    peopleAttending = 0
    hotDogs = 0
    
    #number of people attending the cookout
    peopleAttending = getInteger("Please enter the number of people attending cookout:")
    
    #number of hotdogs per person
    hotDogs = getInteger("Please enter the number of hot dogs each person would like:")
    
    #total amount of hotdogs per person
    total = peopleAttending * hotDogs
    return total
    
# minimum amount of hotdogs and hotdog buns needed and how many of each are left over
def showResults(minDogs, minBuns, dogsLeft, bunsLeft):
    
    print("\nMinimum packagess of hot dogs needed:", minDogs)

    print("\nMinimum packages of hot dog buns needed:", minBuns)

    print("\nHot dogs left over:",dogsLeft)

    print("\nHot dog buns left over:", bunsLeft)
    
    return
    
#integer input validation 
def getInteger(message):
    while True:
        try:
            peopleAttending = int(input(message))
            return peopleAttending 
        except ValueError:
            print("\nIncorrect data entered, please re-attempt")
            
def getInteger(message):
    while True:
        try:
            hotDogs = int(input(message))
            return hotDogs
        except ValueError:
            print("\nIncorrect data entered, please re-attempt")
main()
