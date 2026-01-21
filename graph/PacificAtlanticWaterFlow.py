from typing import List

'''
    417. Pacific Atlantic Water Flow
    
    Use DFS to find all cells that can reach both oceans.
    Use a set to track visited cells from each ocean.
    
    Return the intersection of the two sets.
    
    Time Complexity: O(M * N)
    Space Complexity: O(M * N)
'''

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visited, prev_height):
            key = (r,c)
            if key in visited or r < 0 or r == ROWS or c < 0 or c == COLS or heights[r][c] < prev_height:
                return
            
            visited.add(key)

            dfs(r - 1, c, visited, heights[r][c])
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
        
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])
        

        return list(pac & atl)

# Testcases:
sol = Solution()
print(sol.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]) == [(4, 0), (0, 4), (3, 1), (1, 4), (3, 0), (2, 2), (1, 3)])
print(sol.pacificAtlantic([[1]]) == [(0,0)])