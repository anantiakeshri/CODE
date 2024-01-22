# 26. Remove Duplicates from Sorted Array

nums = [1,1,2]
# Output: 2, nums = [1,2,_]

def removeDuplicate(nums):
    j = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[j] = nums[i]
            j += 1
    return j

print(removeDuplicate(nums))