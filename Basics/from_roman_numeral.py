def from_roman_numeral(roman_numeral):
    romanDic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    answer = 0

    for i in range(len(roman_numeral) - 1):

        if romanDic[roman_numeral[i]] < romanDic[roman_numeral[i + 1]]:
            answer = answer - romanDic[roman_numeral[i]]
        else:
            answer = answer + romanDic[roman_numeral[i]]

    answer = answer + romanDic[roman_numeral[- 1]]

    print(answer)
    return answer


from_roman_numeral('M')
