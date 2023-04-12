def sum_primes(n):
    total = 0

    for j in range(0, n):
        if isPrime(j):
            total += j
    print(total)
    return total


def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    print("true")
    return True

isPrime(2)