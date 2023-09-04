# Search Insert Position - 35

""" Input: """ 
nums = [1,3,5,6] 
target = 5
# Output: 2


""" Input: """ 
# nums = [1,3,5,6] 
# target = 2
# Output: 1


class Solution:
    def searchInsert(nums, target):
        for i, num in enumerate(nums):
            if target <= num:
                return i
        return len(nums)   
    
    print(searchInsert(nums, target))    
