from typing import List

class Solution:
    def partition(self, nums, low, high):
        pivot = nums[high]
        i = low - 1
        j = low
        while j < high:
            if nums[j] < pivot:
                i += 1
                nums[j],nums[i] = nums[i],nums[j]
            j += 1
        
        nums[i + 1],nums[high] = nums[high],nums[i + 1]

        return i + 1

    def quickSort(self, nums: List[int], low, high):
        if low >= high:
            return
        
        pi = self.partition(nums, low, high)

        self.quickSort(nums, low, pi - 1)
        self.quickSort(nums, pi + 1, high)

    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []
        n = len(changed)
        self.quickSort(changed, 0, n - 1)

        original = []
        i = 0
        while i < len(changed):
            originalValue = changed[i]
            double = originalValue * 2
            try:
                doubleIndex = changed.index(double, i + 1)
                changed.pop(doubleIndex)
                original.append(originalValue)
            except (ValueError, IndexError):
                original = []
                break
            
            i += 1


        if len(original) == n / 2:
            return original
        
        return []

solution = Solution()
# Tests
# Testcase 1
originalArr = solution.findOriginalArray([40,7,78,12,40,28,33,27,35,90,56,44,42,38,36,3,12,68,86,14,27,80,33,40,12,74,20,50,15,54,76,13,40,3,43,88,14,54,20,0,100,10,23,30,27,50,84,24,15,45,94,66,6,22,20,34,25,100,28,6,37,10,18,82,96,0,76,40,32,33,48,70,24,80,20,40,50,4,19,25,66,38,46,44,98,47,26,54,38,39,41,20,49,8,16,6,50,30,20,66])
expected = [0,3,3,4,6,7,10,10,12,12,13,14,15,15,16,18,19,20,20,20,20,22,23,25,25,27,27,27,28,33,33,33,34,35,37,38,38,39,40,40,41,42,43,44,45,47,48,49,50,50]

print(originalArr == expected)