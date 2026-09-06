def fibonacci(n):
    a = 0
    b = 1

    print(a)
    print(b)

    for i in range(n - 2):
        next_number = a + b 
        print (next_number)
        a = b 
        b = next_number

fibonacci(10)


 