#In this problem, you are given an array that represents a flowerbed,
#where each element in the array can either be 0 or 1. An element with a value of 0 implies that the corresponding plot in the flowerbed is empty,
#while an element with a value of 1 suggests that there is a flower already planted in that plot.
#The challenge is to plant new flowers (represented by n) in the empty plots under the condition that no two flowers can be adjacent to each other. 
#If it's possible to plant n new flowers following this rule, you must return true, otherwise, you return false.

#The key to solving this problem is:
#understanding that you can plant a flower in the current empty plot (i) only if both the preceding (i - 1) and following (i + 1) plots are also empty. 


def canPlaceFlowers(flowerbed, n):

    flowerbed = [0] + flowerbed + [0]

    for i in range(1, len(flowerbed) - 1):
        if sum(flowerbed[i-1 : i+2]) == 0:
            flowerbed[i] = 1
            n -= 1
            if n ==0:
                return True
    return n <= 0

x = list(map(int, input().split())) #input can only be in the form of 0's and 1's
y = int(input())

place = canPlaceFlowers(x, y)
print(place)
