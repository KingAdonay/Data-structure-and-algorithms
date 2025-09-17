from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        n = len(prices)
        if n == 1:
            return 0
        
        left = 0
        for right in range(1, n):
            profit = prices[right] - prices[left]
            if profit > 0:
                max_profit = max(max_profit, profit)
            if prices[left] > prices[right]:
                left = right
        
        return max_profit

    def maxProfit_dp(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0

        min_price = prices[0]
        dp = [0] * n  # dp[i] stores max profit up to day i

        for i in range(1, n):
            min_price = min(min_price, prices[i])
            dp[i] = max(dp[i-1], prices[i] - min_price)

        return dp[-1]
    
# Tests
sol = Solution()
# Testcase 1: [7,1,5,3,6,4]
print(sol.maxProfit([7,1,5,3,6,4]) == 5)
# Testcase 2: [7,6,4,3,1]
print(sol.maxProfit([7,6,4,3,1]) == 0)


# Testcase 3: [7,1,5,3,6,4]
print(sol.maxProfit_dp([7,1,5,3,6,4]) == 5)
# Testcase 4: [7,6,4,3,1]
print(sol.maxProfit_dp([7,6,4,3,1]) == 0)