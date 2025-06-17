from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        n = len(nums)
        for i in range(n):
            if nums[i] != 0:
                if nums[j] != nums[i]:
                    nums[j], nums[i] = nums[i], nums[j]
                j += 1
            

# Tests
sol = Solution()
# Testcase 1: [0,1,0,3,12]
nums = [0,1,0,3,12]
sol.moveZeroes(nums)
print(nums == [1,3,12,0,0])
# Testcase 2: [2,1]
nums = [2,1]
sol.moveZeroes(nums)
print(nums == [2,1])
# Testcase 3: [1,0,1]
nums = [1,0,1]
sol.moveZeroes(nums)
print(nums == [1,1,0])
