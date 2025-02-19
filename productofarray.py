#The problem provided relates to an array transformation challenge. Specifically, you are given an integer array named nums and the task is to generate a new array named answer. For each index i in the new array, answer[i] should be the product of all the elements in nums except for nums[i]. For example, if nums = [1, 2, 3, 4], then answer = [24, 12, 8, 6] because:

# answer[0] should be 2*3*4 = 24
# answer[1] should be 1*3*4 = 12
# answer[2] should be 1*2*4 = 8
# answer[3] should be 1*2*3 = 6

#The implementation of the solution leverages a single-dimensional array for storage and two variables for the accumulation of products. The algorithm does not use complex data structures or patterns; instead, it builds on the simple principle of accumulation and iteration over the input array.

def productExceptSelf(nums):
        nl = len(nums)
        result = [1] * nl
        left = 1
        for i in range(nl):
            result[i] = left
            left *= nums[i]
        
        right = 1
        for i in range(nl-1, -1, -1):
            result[i] *= right
            right *= nums[i]
        
        return result

x = list(map(int, input().split()))
y = productExceptSelf(x)
print(y)