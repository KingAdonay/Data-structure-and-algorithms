from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        storage = {}

        def helper(i: int, is_buy: bool) -> int:
            if i >= n:
                return 0
            
            tup = (i, is_buy)
            if tup in storage:
                return storage[tup]
            
            if is_buy:
                storage[tup] = max((-prices[i] + helper(i+1, False)), helper(i+1, True))
            else:
                storage[tup] = max(prices[i] + helper(i+2, True), helper(i+1, False))

            return storage[tup]
        
        return helper(0, True)
    
# Tests
sol = Solution()
# Testcase 1: [1,2,3,0,2]
print(sol.maxProfit([1,2,3,0,2]) == 3)
# Testcase 2: [1]
print(sol.maxProfit([1]) == 0)
# Testcase 3: [1,2,4]
print(sol.maxProfit([1,2,4]) == 3)
# Testcase 4: [6,1,3,2,4,7]
print(sol.maxProfit([6,1,3,2,4,7]) == 6)