def fibonacci(n): # defines fibonacci as a function where n is the number of digits we want
    a = 0 # assigns 0 to the variable a 
    b = 1 # assigns 1 to the varraible b

    print(a) # prints the value of a in the terminal
    print(b) # prints the value of b in the terminal 

    for i in range(n - 2): # this line essentially creats a loop for the function or code under it
        next_number = a + b # this is the start of the code where we assign a value to next_number
        print (next_number) # self exmplanitory but I did want to include since we print the first
        # numbers thats why we include that n - 2 

        a = b 
        b = next_number

fibonacci(10) # prints the function in the terminal


 