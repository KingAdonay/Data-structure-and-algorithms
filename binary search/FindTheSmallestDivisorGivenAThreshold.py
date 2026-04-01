from typing import List
from math import ceil

'''
    1283. Find the Smallest Divisor Given a Threshold
    
    Use binary search to find the smallest divisor such that the sum of the division results is less than or equal to the threshold.
    
    Intuition:
    - If the sum of the division results with the current divisor is less than or equal to the threshold, it means we can try smaller divisors to see if we can still meet the threshold, so we move the right pointer to mid.
    - If the sum is greater than the threshold, it means we need a larger divisor to reduce the sum, so we move the left pointer to mid + 1.
    
    Time Complexity: O(n log(m)) where n is the length of nums and m is the maximum value in nums, since we perform binary search on the range of possible divisors and for each divisor we calculate the sum which takes O(n) time.
    Space Complexity: O(1) since we only use a constant amount of extra space.
'''

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def getSum(divisor):
            summ = 0
            for num in nums:
                summ += ceil(num/divisor)
            
            return summ
        
        left, right = 1, max(nums)
        while left < right:
            mid = (left + right) // 2
            summ = getSum(mid)
            if summ <= threshold:
                right = mid
            else:
                left = mid + 1
        
        return right
    
# Testcases
sol = Solution()
# Testcase 1: nums = [1,2,5,9], threshold = 6 -> 5
nums1 = [1,2,5,9]
threshold1 = 6
print(sol.smallestDivisor(nums1, threshold1) == 5)
# Testcase 2: nums = [2,3,5,7,11], threshold = 11 -> 3
nums2 = [2,3,5,7,11]
threshold2 = 11
print(sol.smallestDivisor(nums2, threshold2) == 3)
# Testcase 3: nums = [19], threshold = 5 -> 4
nums3 = [19]
threshold3 = 5
print(sol.smallestDivisor(nums3, threshold3) == 4)  