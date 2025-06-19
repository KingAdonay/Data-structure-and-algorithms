from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i, j = 0, 0
        n = len(nums)
        flips = k
        max_len = 0
        while j < n:
            if nums[j] == 0:
                flips -= 1
            
            while flips < 0:
                if nums[i] == 0:
                    flips += 1
                i += 1
            
            max_len = max(max_len, j - i + 1)
            j += 1
        
        return max_len

# Tests
sol = Solution()
# Testcase 1:
nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
print(sol.longestOnes(nums, k) == 10)
# Testcase 2:
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(sol.longestOnes(nums, k) == 6)