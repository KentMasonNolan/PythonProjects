
def isPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    # print(n)
    # print("true")
    return True

# isPrime(3)


for x in range(222281, 222381):
    b = ((bin(x)).count("1"))
    if isPrime(b):
        print(x )

