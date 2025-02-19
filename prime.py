def isprime(num):
    for i in range(2, num):
        if num%i == 0:
            return False
    return True

def prime_gen(n):
    num = 2
    while n:
        if isprime(num):
            yield num
            n -=1
        num += 1

x = int(input("Enter the number of prime nos required"))

gen = prime_gen(x)
print("Here is your required list: ")
for e in gen:
    print(e, end = " ")