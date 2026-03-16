from typing import List

''' 
    695. Max Area of Island
    
    Use DFS to explore the area of each island.
    Mark visited land cells as water to avoid counting them multiple times.
    
    Time Complexity: O(ROWS * COLS) since we may visit each cell at most once
    Space Complexity: O(ROWS * COLS) in the worst case if the grid is filled with land
'''

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(row: int, col: int) -> int:
            if row < 0 or row == ROWS or col < 0 or col == COLS:
                return 0

            if grid[row][col] == 0:
                return 0
            
            area = 1
            grid[row][col] = 0
            for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                area += dfs(row + i, col + j)
            
            return area
        
        max_area = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    max_area = max(max_area, dfs(row, col))
        
        return max_area
    
# Testcases:
sol = Solution()
print(sol.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]) == 6)
print(sol.maxAreaOfIsland([[0,0,0,0,0,0,0,0]]) == 0)
print(sol.maxAreaOfIsland([[0,0,0,1,1,0,0,0]]) == 2)
print(sol.maxAreaOfIsland([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]) == 4)