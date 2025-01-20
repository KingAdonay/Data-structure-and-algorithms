from typing import List

class Solution:
    def countingSort(self, heights: List[int]) -> List[int]:
        n = len(heights)
        countArr = [0] * 101

        for height in heights:
            countArr[height] += 1
        
        for i in range(1, 101):
            countArr[i] += countArr[i - 1]
        
        j = n - 1
        newArr = [0] * n
        while j >= 0:
            countArr[heights[j]] -= 1
            newArr[countArr[heights[j]]] = heights[j]
            j -= 1

        return newArr

    def heightChecker(self, heights: List[int]) -> int:
        sortedHeights = self.countingSort(heights)
        count = 0

        for i, height in enumerate(heights):
            if height != sortedHeights[i]:
                count += 1

        return count


# Tests
solution = Solution()
# Testcase 1: [1,1,4,2,1,3], expected = 3
actual = solution.heightChecker([1,1,4,2,1,3])
print(actual == 3)
# Testcase 2: [5,1,2,3,4], expected = 5
actual = solution.heightChecker([5,1,2,3,4])
print(actual == 5)
# Testcase 3: [1,1,4,2,1,3], expected = 0
actual = solution.heightChecker([1,2,3,4,5])
print(actual == 0)