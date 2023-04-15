def filtered(iterable, filter_func):
    filtered_list = list(filter(filter_func, iterable))
    return filtered_list


if __name__ == '__main__':
    # Test filtered function with lambda expressions
    items = [1, 2, 3, 4, 5, 6]
    even = filtered(items, lambda x: x % 2 == 0)
    odds = filtered(items, lambda x: x % 2 == 1)
    # print("Even numbers:", even)
    # print("Odd numbers:", odds)

    # Print numbers from 0 to 100 that are multiples of 3, 5, and 15
    numbers = list(range(101))
    multiples_of_3 = filtered(numbers, lambda x: x % 3 == 0)
    multiples_of_5 = filtered(numbers, lambda x: x % 5 == 0)
    multiples_of_15 = filtered(numbers, lambda x: x % 15 == 0)
    resultString = ', '.join(map(str, multiples_of_3))
    print(resultString)
    resultString = ', '.join(map(str, multiples_of_5))
    print(resultString)
    resultString = ', '.join(map(str, multiples_of_15))
    print(resultString)

