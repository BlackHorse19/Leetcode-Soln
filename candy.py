def kidsWithCandies(candies, extraCandies):

    maxC = max(candies)
    result = []
    for i in candies:
        if i + extraCandies >= maxC:
            result.append(True)
        else:
            result.append(False)
    return result

x = list(map(int, input().split())) #while giving the input in terminal use spaces for each integer
y = int(input())

a = kidsWithCandies(x, y)
print(a)
