from typing import List

'''
    39. Combination Sum
    
    Solution using Recursion + Backtracking
    
    Time complexity: O(N^T) where N is number of candidates and T is target
    Space complexity: O(T) for the recursion stack
'''

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)

        def helper(arr, i, summ):
            if summ > target:
                return

            if summ == target:
                res.append(arr)
                return

            for j in range(i, n):
                helper(arr + [candidates[j]], j, summ + candidates[j])

        helper([], 0, 0)
        return res

# Testcases:
sol = Solution()
print(sol.combinationSum([2,3,6,7], 7)) # [[7],[2,2,3]]
print(sol.combinationSum([2,3,5], 8)) # [[2,2,2,2],[2,3,3],[3,5]]
print(sol.combinationSum([2], 1)) # []  