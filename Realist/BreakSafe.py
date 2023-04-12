num = [1, 5, 8]

code = [0, 0, 0, 0]

for i in range(len(num)):
    code[0] = num[i]
    for j in range(len(num)):
        code[1] = num[j]
        for k in range(len(num)):
            code[2] = num[k]
            for l in range(len(num)):
                code[3] = num[l]
                if set(list(code)) == set(list(num)):
                    print(' '.join(str(e) for e in code))


