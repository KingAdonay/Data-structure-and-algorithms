from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        countArr = []
        numsLength = len(nums)

        for i in range(numsLength):
            countArr.append(0)

        for i in range(numsLength):
            for j in range(numsLength):
                if (nums[j] < nums[i]):
                    countArr[i] += 1

        return countArr
    
    def smallerNumbersThanCurrentOptimal(self, nums: List[int]) -> List[int]:
        result = []

        countArr = [0] * 101
        for num in nums:
            countArr[num] += 1
        
        for i in range(1, 101):
            countArr[i] += countArr[i - 1]

        j = len(countArr) - 1
        
        while j > 0:
            countArr[j] = countArr[j - 1]
            j -= 1
        
        for num in nums:
            if num == 0:
                result.append(0)
                continue
            result.append(countArr[num])

        return result
    
    def checkValues(self, actualValue, expectedValue):
        for i, value in enumerate(actualValue):
            if (expectedValue[i] != value):
                print("Test failed.")
                return
        print("Test passed.")
        

solution = Solution()

# Tests
# Testcase 1: [8,1,2,2,3]
result = solution.smallerNumbersThanCurrent([8,1,2,2,3])
solution.checkValues(result, [4,0,1,1,3])

# Testcase 2: [7,7,7,7]
result = solution.smallerNumbersThanCurrentOptimal([7,7,7,7])
solution.checkValues(result, [0,0,0,0])