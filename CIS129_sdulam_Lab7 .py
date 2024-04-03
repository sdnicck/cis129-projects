# Satya Dulam
# 4/2/14
# Lab 7: Calculator to add up total amount of revenue 

#A dramatic theater has three seating sections, and it charges the following prices for tickets in each section: section A seats cost $20 each, section B seats cost $15 each, and section C seats cost $10 each. The theater has 300 seats in section A, 500 seats in section B, and 200 seats in section C. Design a program that asks for the number of tickets sold in each section and then displays the amount of income generated from ticket sales. The program should validate the numbers that are entered for each section.

#A program that does not work, or crashes, will earn 0 points for the assignment.

#Write generalized routines. Do not have any hardcoded "A", "B", "C" outside of Main.

#Pass variables to generalized functions that return a value.

#ALL numbers in the problem statement MUST be stored in named constants. The section names should also be constants: A, B, C

#Design the program so it will be relatively easy to add a section D to the program by adding some constants and a few statements in main.

#Design the program so it will be easy to change the number of seats in each section or the cost of a seat in each section.

#Display a welcome message with all the constant values (not hardcoded)

#Give a subtotal for all purchases so far after each new purchase

#Display the overall total at the end of the program, and the number of seats and subtotals for each section


def main():
    
    print()
    
    runProgram = 1

    while runProgram == 1:
        
    # cost of seat per section
        COSTA = 20
        COSTB = 15
        COSTC = 10
    
    #total number of seats in a section (max number for each section)
        LOWSECTIONA = 0
        LOWSECTIONB = 0
        LOWSECTIONC = 0
        SEATTOTALA = HIGHSECTIONA = 300
        SEATTOTALB = HIGHSECTIONB = 500
        SEATTOTALC = HIGHSECTIONC = 200
        
        ticketsA, ticketsB, ticketsC = totalTickets()
    
    #setting variables for total amount of income per section and total 
        sectionAIncome = 0
        sectionBIncome = 0
        sectionCIncome = 0
        totalTheaterIncome = 0
    
    #functions for total income per section 
        sectionAIncome = ticketsA * COSTA
        sectionBIncome = ticketsB * COSTB
        sectionCIncome = ticketsC * COSTC 
    
    #function for total income for whole theater 
        totalTheaterIncome = sectionAIncome + sectionBIncome + sectionCIncome
    
    #call to results 
        showResults(sectionAIncome, sectionBIncome, sectionCIncome, totalTheaterIncome)
        
        runProgram = getValidNum("\nDo you want to enter in more data? (1 for yes or 2 for no):",1,2)
    
#function to collect total tickets sold 
def totalTickets():
    print("\nPlease enter the total tickets sold of seats in each section of the theater.\n   Section A has 300 seats avaliable that are sold tickets for $20 each\n   Section B has 500 seats avaliable that are sold tickets for $15 each\n   Section A has 200 seats avaliable that are sold tickets for $20 each\n")
    #setting variable  total tickets sold per section
    ticketsA = 0
    ticketsB = 0
    ticketsC = 0
    
    #collecting total tickets sold from user
    ticketsA = getValidNum("\nPlease enter the total number of seats sold for section A of the theater:", 0, 300)
    ticketsB = getValidNum("\nPlease enter the total number of seats sold for section B of the theater:", 0, 500)
    ticketsC = getValidNum("\nPlease enter the total number of seats sold for section C of the theater:", 0, 200)
    return ticketsA, ticketsB, ticketsC

    #showing results of income 
def showResults(sectionAIncome, sectionBIncome, sectionCIncome, totalTheatherIncome):
    print("\nThe subtotal income from section A is $", sectionAIncome)
    print("\nThe subtotal income from section B is $", sectionBIncome)
    print("\nThe subtotal income from section C is $", sectionCIncome)
    print("\nThe total income from the theater is $", totalTheatherIncome)
    return 

    # integer input validation 
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
