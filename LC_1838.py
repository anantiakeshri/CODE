# 1838. Frequency of the Most Frequent Element

nums = [1,2,4]
k = 5
# Output: 3

def maxFrequency(nums, k):
    nums.sort()
    left = right = res = total = 0

    while right < len(nums):
        total += nums[right]

        while nums[right] * (right - left + 1) > total + k:
            total -= nums[left]
            left += 1
        
        res = max(res, right - left + 1)
        right += 1
    
    return res
      
print(maxFrequency(nums, k))