# Leet Code - Number of Good Pairs - Ques 1512

# Input: 
nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

""" Approach 1 -  Hashmap """
def numIdenticalPairs(nums) -> int:
    pairs = {}
    count = 0
    for num in range(len(nums)):
        if nums[num] in pairs:
            count += pairs[nums[num]]
    
        pairs[nums[num]] = pairs.get(nums[num], 0) + 1

    return count

print(numIdenticalPairs(nums))

""" Approach 2 """
# def numIdenticalPairs(nums) -> int:
#     count = 0
#     n = len(nums)
#     for i in range(n):
#         for j in range(i + 1, n):
#             if nums[i] == nums[j]:
#                 count += 1
                
#     return count

# print(numIdenticalPairs(nums))
