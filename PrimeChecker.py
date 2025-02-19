def isprime(num):
    for i in range(2, num):
        if num % i == 0:
            return 'Not a prime'
        else:
            return 'Is a prime'
        

x = int(input("Enter your number:" ))

check = isprime(x)
print(check)