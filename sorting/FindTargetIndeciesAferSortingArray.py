from typing import List

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        countArr = [0] * 101
        sortedNums = [None] * len(nums)
        indecies = []

        for num in nums:
            countArr[num] += 1

        for i in range(1, 101):
            countArr[i] = countArr[i - 1] + countArr[i]
        
        j = len(nums) - 1

        while j >= 0:
            countArr[nums[j]] -= 1
            sortedNums[countArr[nums[j]]] = nums[j]

            j-=1
        
        k = 0
        while k < len(sortedNums):
            if target == sortedNums[k]:
                indecies.append(k)
            if sortedNums[k] != None and sortedNums[k] > target:
                break
            k+=1
        
        return indecies
        
    def checkValues(self, actualValue, expectedValue):
        for i, value in enumerate(actualValue):
            if (expectedValue[i] != value):
                print("Test failed.")
                return
        print("Test passed.")

solution = Solution()

# Tests
# Testcase 1: nums: [1,2,5,2,3], target: 2
result = solution.targetIndices([1,2,5,2,3], 2)
solution.checkValues(result, [1, 2])

# Testcase 2: nums: [1,2,5,2,3], target: 5
result = solution.targetIndices([1,2,5,2,3], 5)
solution.checkValues(result, [4])

# Testcase 3: nums: [1], target: 1
result = solution.targetIndices([1], 1)
solution.checkValues(result, [0])

# Testcase 4: nums: [100, 1], target: 1
result = solution.targetIndices([100, 1], 1)
solution.checkValues(result, [0])