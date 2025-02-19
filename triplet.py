#The problem gives us an array of integers, nums, and asks us to determine if it is possible to find a sequence of three elements, where each element comes after the previous one in the order they appear in the array (i.e., they have increasing indices), and each element is greater than the one before it in this sequence. This sequence should satisfy the condition nums[i] < nums[j] < nums[k], where i, j, and k are the indices of these elements in the array, such that i < j < k. If such a sequence exists in nums, the function should return true, otherwise, it should return false.

#To arrive at the solution efficiently, instead of looking for the whole triplet right away, we can keep track of the smallest number we have encountered so far (mi) and a middle number that is greater than mi but smaller than any potential third number (mid). As we iterate through the array, we can update these two numbers whenever possible. The idea here is to maintain the lowest possible values for mi and mid as we move forward, giving us the best chance to find a number that would be greater than both, thus forming our triplet.

def triplet(num):
    small = mid = float('inf')

    for i in num:
        if i <= small:
            small = i
        elif i <= mid:
            mid = i
        else:
            return True
    return False

x = list(map(int, input().split()))
y = triplet(x)
print(y)