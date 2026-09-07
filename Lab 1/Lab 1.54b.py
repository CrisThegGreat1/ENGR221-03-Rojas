
def parking_fee(n): # defines parking_fee(n) as a function 
    cost = (n * 3) # assigns a value to cost
    if n <=1: # accounts for first hour free parking
        return "$0"
    if cost < 20: # assigns a maximum value that can be charged 
        return f"${cost}" # returns the value of cost with the dollar sign in front
    else:
        return "$20"

parking_fee(20) # gives a value to n

print(parking_fee(20)) # prints the value of the function