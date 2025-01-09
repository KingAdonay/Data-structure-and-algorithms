from typing import List


class Solution:
    def countingSort(self, nums:List[str], countPointerIdx: int) -> List[str]:
        countArr = [0] * 10

        for num in nums:
            digit = 0
            if len(num) >= countPointerIdx:
                digit = int(num[-1 * countPointerIdx])
            countArr[digit] += 1
        
        i = 1
        while i < len(countArr):
            countArr[i] += countArr[i - 1]
            i += 1
        
        i = len(nums) - 1
        sortedNums = [None] * len(nums)

        while i >= 0:
            num = nums[i]
            digit = 0
            if len(num) >= countPointerIdx:
                digit = int(num[-1 * countPointerIdx])
            
            countArr[digit] -= 1
            sortedNums[countArr[digit]] = num
            i -= 1

        return sortedNums
    
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        maxLength = 1
        for num in nums:
            if len(num) > maxLength:
                maxLength = len(num)

        for countPointerIdx in range(1, maxLength+1):
            nums = self.countingSort(nums, countPointerIdx)
        
        return nums[-k]
        

# Tests
solution = Solution()

# Testcase 1: ["3","6","7","10"], k = 4, expected = "3"
kthLargestNumber = solution.kthLargestNumber(["3","6","7","10"], 4)
print(kthLargestNumber == "3")
# Testcase 2: ["3000","600","700","10", "1", "100", "1", "0"], k = 4, expected = "100"
kthLargestNumber = solution.kthLargestNumber(["3000","600","700","10", "1", "100", "1", "0"], 4)
print(kthLargestNumber == "100")