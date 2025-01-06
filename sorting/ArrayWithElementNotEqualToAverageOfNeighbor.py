from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums) - 1:
            if (i % 2 == 0 and nums[i] <= nums[i + 1]) or (i % 2 != 0 and nums[i] >= nums[i + 1]):
                nums[i], nums[i + 1] = nums[i + 1], nums[i]

            i += 1
        
        return nums
    

# Tests
def assertArrays(actualValue, expectedValue):
    for i, value in enumerate(actualValue):
        if (expectedValue[i] != value):
            print("Test failed.")
            return
    print("Test passed.")  



solution = Solution()

# Testcase 1: [1,2,3,4,5]
wiggledArr = solution.rearrangeArray([1,2,3,4,5])
assertArrays(wiggledArr, [2,1,4,3,5])

# Testcase 2: [6,2,0,9,7]
wiggledArr = solution.rearrangeArray([6,2,0,9,7])
assertArrays(wiggledArr, [6,0,9,2,7])