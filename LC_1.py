#  Leet Code - Ques 1 - Two Sum

nums = [3,2,4]
target = 6
# Output: [1,2]

# nums = [2,7,11,15]
# target = 9
# # Output: [0,1]

""" Approach 1 - Not optimized - 16/60 TC pass"""
def twoSum(self, nums, target):
    i = 0
    j = (len(nums) - 1)
    for index, _ in enumerate(nums):
        sum = nums[i] + nums[j]
        if sum == target:
            return i, j
        elif sum < target:
            i = i + 1
        else:
            j = j - 1


""" Approach 2 = HashMap"""
def twoSum(self, nums, target):
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return([seen[target - num], i])
        elif num not in seen:
            seen[num] = i

print(nums, target)