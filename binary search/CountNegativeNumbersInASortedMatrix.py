
from typing import List


'''    
    1351. Count Negative Numbers in a Sorted Matrix
    
    Use binary search to find the starting index of negative numbers in each row, and count the number of negative numbers based on that index.
    
    Time Complexity: O(ROWS * log(COLS)) since we perform binary search for each row
    Space Complexity: O(1) since we only use a constant amount of extra space
'''
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        def get_neg_start(row):
            left, right = 0, COLS - 1
            
            while left <= right:
                mid = (left + right) // 2

                if grid[row][mid] < 0:
                    right = mid - 1
                else:
                    left = mid + 1
            
            return left
        
        count = 0
        for row in range(ROWS):
            col_start = get_neg_start(row)

            if 0 <= col_start < COLS:
                count += COLS - col_start
        
        return count
        

# Testcases
sol = Solution()
# Testcase 1: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]] -> 8
grid1 = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
print(sol.countNegatives(grid1) == 8)
# Testcase 2: grid = [[3,2],[1,0]] -> 0
grid2 = [[3,2],[1,0]]
print(sol.countNegatives(grid2) == 0)
# Testcase 3: grid = [[1,-1],[-1,-1]] -> 3
grid3 = [[1,-1],[-1,-1]]
print(sol.countNegatives(grid3) == 3)