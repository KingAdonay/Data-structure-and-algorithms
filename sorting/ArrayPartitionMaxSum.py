from typing import List


class Solution:
    def partition(self, nums: List[int], left: int, right: int) -> int: 
        pivot = nums[right]
        i = left - 1
        j = left
        while j < right:
            if nums[j] < pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
            j += 1
        
        pi = i + 1
        nums[pi], nums[right] = nums[right], nums[pi]

        return pi

    def quickSort(self, nums: List[int], left: int, right: int):
        if left >= right:
            return 
        
        pi = self.partition(nums, left, right)

        self.quickSort(nums, left, pi - 1)
        self.quickSort(nums, pi + 1, right)

    def arrayPairSum(self, nums: List[int]) -> int:
        self.quickSort(nums, 0, len(nums) - 1)

        sum = 0
        i = 0
        while i < len(nums):
            sum += nums[i]
            i += 2

        return sum

solution = Solution()
# Tests
# Testcase 1: [1,4,3,2], 4
actual = solution.arrayPairSum([1,4,3,2])
print(actual == 4)
# Testcase 2: [6,2,6,5,1,2], 9
actual = solution.arrayPairSum([6,2,6,5,1,2])
print(actual == 9)