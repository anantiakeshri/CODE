# Ques 27 - Remove Element

nums = [3,2,2,3]
val = 3
# Output: 2, nums = [2,2,_,_]

def removeElement(nums, val):
    index = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[index] = nums[i]
            index += 1
    return index

print(removeElement(nums, val))