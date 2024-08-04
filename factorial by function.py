def fact(num):
    fac = 1
    for x in range(1, num+1):
        fac *= x
    print("Factorial of number is:", fac)

num = int(input("Enter a positive number: "))    
fact(num)