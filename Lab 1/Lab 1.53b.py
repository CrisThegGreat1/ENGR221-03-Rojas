def change(n): # defines change as a function
    quarter = 25 # assigns value
    dime = 10  
    nickle = 5
    penny = 1
    quarters_used = n // quarter #divides change by the value of quarters
    n = n - (quarters_used * quarter) # accounts for the new value of n after the division
    dimes_used = n // dime # divides by the value of dime
    n = n - (dimes_used * dime)
    nickles_used = n // nickle
    n = n - (nickles_used * nickle)
    pennies_used = n // penny 
    return quarters_used + dimes_used + nickles_used + pennies_used 
# adds all the amount of coins used and returns the number
change(72) # assigns a value to n 

print(change(72)) # prints the amount of coins used
