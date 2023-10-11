#  Leet Code - Ques 1 - Two Sum

nums = [3,2,4]
target = 6
# Output: [1,2]

# nums = [2,7,11,15]
# target = 9
# # Output: [0,1]

""" Approach 1 - HashMap - Sliding Window Technique """
def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return([seen[target - num], i])
        elif num not in seen:
            seen[num] = i

print(twoSum(nums, target))