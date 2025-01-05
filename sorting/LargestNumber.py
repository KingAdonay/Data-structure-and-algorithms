import math
from typing import List

class Solution:
    def merge(self, nums: List[str], start: int, mid: int, end: int):
        n1 = mid - start + 1
        n2 = end - mid

        leftArr = []
        rightArr = []

        i = 0
        j = 0
        while i < n1:
            leftArr.append(nums[start + i])
            i += 1

        while j < n2:
            rightArr.append(nums[mid + j + 1])
            j += 1
        
        i = 0
        j = 0
        k = start

        while i < n1 and j < n2:
            if int(leftArr[i] + rightArr[j]) >= int(rightArr[j] + leftArr[i]):
                nums[k] = leftArr[i]
                i += 1
            else: 
                nums[k] = rightArr[j]
                j += 1
            
            k += 1
        
        while i < n1:
            nums[k] = leftArr[i]
            i += 1
            k += 1
        
        while j < n2:
            nums[k] = rightArr[j]
            j += 1
            k += 1

    def mergeSort(self, nums: List[str], start: int, end: int):
        if start >= end:
            return
        
        mid = math.floor(start + (end - start) / 2)
        self.mergeSort(nums, start, mid)
        self.mergeSort(nums, mid + 1, end)

        self.merge(nums, start, mid, end)
    
    def largestNumber(self, nums: List[int]) -> str:
        stringArr = [str(num) for num in nums]
        
        self.mergeSort(stringArr, 0, len(stringArr) - 1)

        return str(int(''.join(stringArr)))
    

# Tests
solution = Solution()

# Testcase 1: [10,2]
largestNum = solution.largestNumber([10,2])
print(largestNum == "210") # print true if result is as expected

# Testcase 2: [3,30,34,5,9]
largestNum = solution.largestNumber([3,30,34,5,9])
print(largestNum == "9534330") # print true if result is as expected

# Testcase 3: [0, 0, 0]
largestNum = solution.largestNumber([0, 0, 0])
print(largestNum == "0") # print true if result is as expected