def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def printPrime(n, m):
    output = ""
    for i in range(n, m):
        if output == "":
            if isPrime(i):
                output += str(i)
        elif isPrime(i):
            output += ", "
            output += str(i)

    print(output)

printPrime(10000, 10050)