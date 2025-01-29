from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        for idx, num in enumerate(nums):
            if num < 0:
                i = idx
                
        j = i + 1
        res = []
        while i >= 0 and j < n:
            if abs(nums[i]) <= nums[j]:
                res.append(nums[i] ** 2)
                i -= 1
            else:
                res.append(nums[j] ** 2)
                j += 1
        
        while i >= 0:
            res.append(nums[i] ** 2)
            i -= 1
        
        while j < n:
            res.append(nums[j] ** 2)
            j += 1
        
        return res
        
# Tests
solution = Solution()
# Testcase 1:
nums = [-4,-1,0,3,10]
expected = [0,1,9,16,100]
actual = solution.sortedSquares(nums)
print(expected == actual)