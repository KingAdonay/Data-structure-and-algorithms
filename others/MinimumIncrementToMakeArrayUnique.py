from typing import List


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()

        count = 0
        maxx = 0
        for i, num in enumerate(nums):
            n = num
            if i > 0 and n <= maxx:
                n = maxx + 1
                count += (n - num)
            
            maxx = max(maxx, n)
        
        return count

# Test
sol = Solution()
# Testcase 1: [1,2,2]
print(1 == sol.minIncrementForUnique([1,2,2]))
# Testcase 2: [1]
print(0 == sol.minIncrementForUnique([1]))
# Testcase 3: [3,2,1,2,1,7]
print(6 == sol.minIncrementForUnique([3,2,1,2,1,7]))