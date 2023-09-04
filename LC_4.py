# Median of Two sorted arrays - 4

# nums1 = [1,3]
# nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

nums1 = [1,2]
nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

class Solution:
    def findMedianSortedArrays(nums1, nums2):
        
        new_num = sorted(nums1+nums2)

        middle = len(new_num) // 2  # Calculate the index of the middle element

        # Check if the total number of elements is even or odd
        if len(new_num) % 2 == 0:
            # If even, return the average of the two middle elements
            return (new_num[middle - 1] + new_num[middle]) / 2
        else:
            # If odd, return the middle element
            return new_num[middle]
        
    print(findMedianSortedArrays(nums1, nums2))

        