from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            for j in range(0, len(nums) - 1 - i):
                if nums[j] > nums[j + 1]:
                    temp = nums[j]
                    nums[j] = nums[j + 1]
                    nums[j+1] = temp
    def checkValues(self, actualValue, expectedValue):
        for i, value in enumerate(actualValue):
            if (expectedValue[i] != value):
                print("Test failed.")
                return
        print("Test passed.")

solution = Solution()
# Tests
# Testcases 1: [2,0,2,1,1,0]
# expected: [0,0,1,1,2,2]
colors = [2,0,2,1,1,0]
solution.sortColors(colors)
solution.checkValues(colors, [0,0,1,1,2,2])