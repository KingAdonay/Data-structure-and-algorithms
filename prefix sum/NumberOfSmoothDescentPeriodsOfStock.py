from typing import List

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        count = 1
        prev = 1
        for i in range(1, n):
            if prices[i - 1] - prices[i] != 1:
               prev = 0
            
            prev += 1
            count += prev
        
        return count


# Tests
sol = Solution()
# Testcase 1:
print(sol.getDescentPeriods([3,2,1,4]) == 7)
# Testcase 2:
print(sol.getDescentPeriods([8,6,7,7]) == 4)
# Testcase 3:
print(sol.getDescentPeriods([4,3,2,1,4]) == 11)