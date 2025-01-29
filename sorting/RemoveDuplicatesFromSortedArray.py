from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        i = 0
        for j in range(n):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        
        return i + 1

# Tests
solution = Solution()
# Testcase 1: nums = [1,1,2]
nums = [1,1,2]
k = solution.removeDuplicates(nums)
print(nums[:k] == [1, 2])

# Testcase 2: nums = [0,0,1,1,1,2,2,3,3,4]
nums = [0,0,1,1,1,2,2,3,3,4]
k = solution.removeDuplicates(nums)
print(nums[:k] == [0, 1, 2, 3, 4])
