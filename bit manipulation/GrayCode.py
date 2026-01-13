from typing import List

'''
    89. Gray code
    
    Use the formula: Gray(i) = i ^ (i >> 1) to generate gray code sequence.
    
    Time complexity: O(2^n)
    Space complexity: O(2^n)
'''

class Solution:
    def grayCode(self, n: int) -> List[int]:
        size = 1 << n
        res = []

        for num in range(size):
            res.append(num ^ (num >> 1))
        
        return res
    
# Testcases
solution = Solution()
print(solution.grayCode(2))  # [0,1,3,2]
print(solution.grayCode(0))  # [0]
print(solution.grayCode(3))  # [0,1,3,2,6,7,5,4]