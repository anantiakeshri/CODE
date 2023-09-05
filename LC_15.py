# 3 SUM - QUestion 15

""" Input 1: """
nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

""" Input 2: """ 
# nums = [0,1,1]
# Output: []

""" Input 3: """
# nums = [0,0,0]
# Output: [[0,0,0]]

class Solution:
    def threeSum(ums):
        triplets = []  # Initialize an empty list to store unique triplets
        nums.sort()    # Sort the input list in ascending order

        for i in range(len(nums) - 2):
            # Skip duplicates in the sorted list
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1  # Initialize two pointers
            while left < right:
                total = nums[i] + nums[left] + nums[right]  # Calculate the sum of the current triplet

                if total == 0:
                    # If the sum is zero, we found a triplet
                    triplets.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move the pointers
                    left += 1
                    right -= 1
                elif total < 0:
                    # If the sum is negative, move the left pointer to the right
                    left += 1
                else:
                    # If the sum is positive, move the right pointer to the left
                    right -= 1
        
        return triplets  # Return the list of unique triplets that sum to zero
    
    print(threeSum(nums))