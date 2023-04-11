def collatz_length(n):
    endNumber = n
    count = 0

    if n <= 1:
        return 0

    while endNumber != 1:
        if endNumber % 2 == 0:
            endNumber = endNumber // 2
        elif endNumber % 2 != 0:
            endNumber = endNumber * 3 + 1
        count += 1
    print(count)

collatz_length(10)