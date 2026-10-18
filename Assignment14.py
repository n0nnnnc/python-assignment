def pascal(n):
    if n == 0:
        return [1]
    elif n == 1:
        return [1, 1]
    else:
        result = [
            1,
        ]
        prevLine = pascal(n - 1)
        for i in range(len(prevLine) - 1):
            sum = prevLine[i] + prevLine[i + 1]
            result.append(sum)
        result.append(1)
        return result


degree = int(input("Please Enter Degree of Pascal Triangle: "))
print(pascal(degree))
print("")
