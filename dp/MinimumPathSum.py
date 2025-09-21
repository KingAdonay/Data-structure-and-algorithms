from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        
        res = [[float('inf')] * (COLS + 1) for r in range(ROWS + 1)]
        
        res[ROWS][COLS-1] = 0

        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                res[r][c] = grid[r][c] + min(res[r + 1][c], res[r][c + 1])
        
        return res[0][0]

# Tests
sol = Solution()
# Testcase 1: [[1,3,1],[1,5,1],[4,2,1]]
print(sol.minPathSum([[1,3,1],[1,5,1],[4,2,1]]) == 7)
# Testcase 2: [[1,2,3],[4,5,6]]
print(sol.minPathSum([[1,2,3],[4,5,6]]) == 12)
# Testcase 3: [[5]]
print(sol.minPathSum([[5]]) == 5)
# Testcase 4: [[1,2],[1,1]]
print(sol.minPathSum([[1,2],[1,1]]) == 3)