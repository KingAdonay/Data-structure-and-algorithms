import math
from typing import List

class Solution:
    def isValidWindow(self, nums, mid, k) -> bool:
        n = len(nums)
        windowSum = 0
        expectedSum = nums[mid - 1] * mid

        for i in range(0, mid):
            windowSum += nums[i]

        if (expectedSum - windowSum) <= k:
            return True
        i = 0
        j = mid
        while j < n:
            windowSum += nums[j]
            windowSum -= nums[i]
            expectedSum = nums[j] * mid

            if (expectedSum - windowSum) <= k:
                return True
            
            j += 1
            i += 1
        
        return False


    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()

        l = 1
        r = len(nums)
        maxFreq = 0

        while l <= r:
            mid = l + (math.floor((r - l) / 2))
            if self.isValidWindow(nums, mid, k):
                maxFreq = max(mid, maxFreq)
                l = mid + 1
            else:
                r = mid - 1


        return maxFreq
        