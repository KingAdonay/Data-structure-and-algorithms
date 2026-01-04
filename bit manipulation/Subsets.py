from typing import List

'''
    78. Subsets
    
    A common approach to generate all possible subsets of a set is to use backtracking or recursion.
    However, a more efficient method involves using bit manipulation.
    Each subset can be represented by a binary number where each bit indicates whether the corresponding element is included in the subset.
    By iterating through all numbers from 0 to 2^n - 1 (where n is the number of elements in the set), we can generate all possible subsets.
    For each number, we check each bit position to determine if the corresponding element should be included in the current subset.
    This approach ensures that we cover all possible combinations of elements in the set.
    
    Example: [1, 2, 3]
    Dry Run:
    i = 0 (000) -> []
    i = 1 (001) -> j = 0 -> [1]
    i = 2 (010) -> j = 1 -> [2]
    i = 3 (011) -> j = 0,1 -> [1,2]
    i = 4 (100) -> j = 2 -> [3]
    i = 5 (101) -> j = 0,2 -> [1,3]
    i = 6 (110) -> j = 1,2 -> [2,3]
    i = 7 (111) -> j = 0,1,2 -> [1,2,3]
    
    Time complexity: O(n * 2^n), where n is the number of elements in the set. We generate 2^n subsets, and for each subset, we may need to iterate through n elements.
    Space complexity: O(1) if we don't consider the output space, otherwise O(n * 2^n) for storing all subsets.
'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        for i in range(1 << n):
            temp = []
            for j in range(n):
                if i & (1 << j):
                    temp.append(nums[j])
            
            res.append(temp)
        
        return res
    
# Testcases:
sol = Solution()
print(sol.subsets([1,2,3]) == [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]])
print(sol.subsets([0]) == [[], [0]])   