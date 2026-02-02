from typing import List

'''
    46. Permutations
    
    Solution using Backtracking
    
    Time complexity: O(N * N!)
    Space complexity: O(N!)
'''

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(path):
            if len(path) == len(nums):
                result.append(path[:]) 
                return

            for num in nums:
                if num in path:   
                    continue
                
                path.append(num)     
                backtrack(path)      
                path.pop()          

        backtrack([])
        return result