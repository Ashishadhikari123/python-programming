number = int(input("Enter a number\n"))
def checkPrime(number):
    if (number == 0):
        print("no it is not a prime number")
        return
    for i in range(2,number):
        if(number%i==0):
            print("Not a prime number")
            return
    print("Yes it is a prime number")
checkPrime(number)
