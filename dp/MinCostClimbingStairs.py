from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        storage = {}
        def helper(i):
            if i >= n:
                return 0

            if i in storage:
                return storage[i]
            
            storage[i] = cost[i] + min(helper(i + 1), helper(i + 2))
            
            return storage[i]
        
        
        return min (helper(0), helper(1))

# Tests
sol = Solution()
# Testcase 1: [10,15,20]
print(sol.minCostClimbingStairs([10,15,20]) == 15)
# Testcase 2: [1,100,1,1,1,100,1,1,100,1]
print(sol.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]) == 6)
