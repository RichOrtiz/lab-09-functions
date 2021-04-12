userNum = input("gimme a number: ")
changedNum = int(userNum)

def factorial(n):
    multiplied = 1
    for i in range(1,n+1):
        #print("works")
        multiplied = multiplied * i;
    return(multiplied)



print(factorial(changedNum))