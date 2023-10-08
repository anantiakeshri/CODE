# Leet Code - Ques 80

nums = [1,1,1,2,2,3]
#output = [1,1,2,2,3]

""" Approach 1 """
# def removeDuplicates(nums):
#     k = 0
#     for i in nums:
#         if k < 2 or i != nums[k-2]:
#             nums[k] = i
#             k += 1
#     return nums, k                    #In Leet code you have to return nums with unique element not appearing more than twice - so just return "K"

# print(removeDuplicates(nums))


""" Approach 2 - 2 pointers"""
def removeDuplicates(nums):
    slow = 2
    fast = 2
    while fast < len(nums):
        if nums[fast] != nums[slow-2]:
            nums[slow] = nums[fast]
            slow += 1
        fast += 1
    return slow, nums       #In Leet code you have to return nums with unique element not appearing more than twice - so just return "slow"

print(removeDuplicates(nums))