#A retail company assigns a $6,000 store bonus if monthly sales are more than $110,000; else if monthly sales are greater than or equal to $100,000 the store bonus is $5,000, else if monthly sales are greater than or equal to $90,000 the store bonus is $4,000, else if monthly sales are greater than or equal to $80,000, the store bonus is $3,000 otherwise a $0 amount or no store bonus is awarded.  They are using a percent of sales increase to determine if employees get individual bonuses.  If sales increased by an amount greater than or equal to 5% (0.05) then all employees get $75, else if sales increased by an amount greater than or equal to 4%, employees get $50, else if sales increased by an amount greater than or equal to 3% employees get $40 otherwise they get $0. 

#storeAmount = the store bonus amount

#empAmount = individual bonus amount 

#salesIncrease = precent of increase

#monthlySales = monthly sales amount


print("What was your store's monthly sales?")
monthlySales = float(input())

#determines the storeAmount bonus
if monthlySales >= 110000:
    storeAmount = 6000
elif monthlySales >= 100000:
    storeAmount = 5000
elif monthlySales >= 90000:
    storeAmount = 4000
elif monthlySales >= 80000:
    storeAmount = 3000
else:
    storeAmount = 0
    
#Determines the percent of increase in sales
print("What was percent increase in sales?")
salesIncrease = float(input())
salesIncrease = salesIncrease/100

#determines the empAmount bonus
if salesIncrease >= 0.05:
    empAmount = 75
elif salesIncrease >=0.04:
    empAmount = 50
elif salesIncrease >=0.03:
    empAmount = 40
else:
    empAmount = 0 
    
# print the bonus information for store and employees
print("The store bonus amount is $",storeAmount,"\nThe employee bonus amount is $",empAmount,)

if storeAmount == 6000 and empAmount == 75:
    print("Congrats! You've reached the highest bonus amounts possible!")
