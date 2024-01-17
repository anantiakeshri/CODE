# Leet Code - Ques 88 - Merge Sorted Array

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
# Output: [1,2,2,3,5,6]

def mergeArray(nums1, m, nums2, n):
    for i in range(m, m + n):
        nums1[i] = nums2[i-m]
    nums1.sort()
    
# Calling of function
mergeArray(nums1, m, nums2, n)
print(nums1)