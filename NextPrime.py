def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


nextPrime = False

while nextPrime == False:
    for i in range(100000000, 200000000):
        if isPrime(i):
            print(i)
            nextPrime = True
            break
