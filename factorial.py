def factorial(n):
    total = 1
    for i in range(0, n):
        total = total * (n - i)
        print("Current i is: " + str(i))
        print("Current value of total is: " + str(total))
    return total


userstring = input("Number please ")
usernum = int(userstring, 10)

print(str(usernum) + "! is " + str(factorial(usernum)))