# Leet Code - Ques 88

nums1 = [0] 
m = 0
nums2 = [1]
n = 1

def mergeArray(nums1, m, nums2, n):
    for i in range(m,m+n):
        nums1[i] = nums2[i-m]
    nums1.sort()
    
print(mergeArray(nums1, m, nums2, n))