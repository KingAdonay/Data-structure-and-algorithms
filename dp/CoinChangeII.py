from typing import List

'''
    518. Coin Change II
    
    The problem can be solved using a recursive approach with memoization to optimize the performance.
    We can define a helper function that takes in the current index of the coins array and the current total amount.
    The base cases for the recursion would be:
    1. If the total amount exceeds the target amount, we return 0 as this is not a valid combination.
    2. If the total amount is equal to the target amount, we return 1 as this is a valid combination.
    3. If we have exhausted all the coins and the total amount is still less than the target amount, we return 0 as this is not a valid combination.
    For each coin, we have two choices: we can either take the coin and add its value to the total amount, or we can skip the coin and move on to the next coin.
    We can recursively call the helper function for both choices and sum up the results to get the total number of combinations.
    To optimize the performance, we can use a cache (dictionary) to store the results of previously computed states (i, total) to avoid redundant calculations.
    
    Time Complexity: O(n * amount), where n is the number of coins and amount is the target amount. This is because we are exploring all combinations of coins and amounts.
    Space Complexity: O(n * amount) due to the recursion stack and the cache storage.
'''
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:        
        cache = {}
        def helper(i: int, total:int) -> int:
            if total > amount or i == len(coins):
                return 0

            if total == amount:
                return 1
            
            key = (i, total)
            if key in cache:
                return cache[key]
            
            take = helper(i, total + coins[i])
            skip = helper(i + 1, total)
            
            cache[key] = take + skip
            return cache[key]
        
        return helper(0, 0)
    
# Testcases:
s = Solution()
print(s.change(5, [1, 2, 3]) == 5)
print(s.change(500, [1, 2, 5]) == 12701)
print(s.change(3, [2]) == 0)
print(s.change(10, [10]) == 1)
