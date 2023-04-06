def dist(points):
    min = -1
    max = 0
    for i in points:
        if min == -1:
            min = i
        elif i < min:
            min = i
    for j in points:
        if j > max:
            max = j

    distance = max - min
    print(distance)
    return distance

dist([1,0.01])