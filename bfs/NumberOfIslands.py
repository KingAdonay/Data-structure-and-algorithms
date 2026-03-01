from typing import List
from collections import deque

'''
    200. Number of islands
    
    Intuition:
    Once we find a land we can be sure it is an island because all the surrounding areas are water, however on all the adjecent sides of a land,
    if there is a connected land, that land should not be counted as a separate island. So what we need to do is, after finding an island,
    we need to find all the connected lands and mark them as visited so that they won't be counted as a separate island.
    We can achieve that by doing a breadth first search on each land and mark all the visited (connected lands) as visited or to minimize the
    space complexity we can just mark all the visited lands as water, that way we won't count them again.
    
    Apprach:
    1. define a bfs helper method that would go throug each adjecent items in the grid and mark the connected lands as water ('0')
    2. traverse the grid and for each element, if it is a land, mark the land as water, increment the number of islands by 1 and do a bfs to
    mark all the lands of the island as water.
    3. return the number of islands
    
    Time complexity: O(m x n), we traverse the whole grid
    Space complexity: O(1), we mark the lands as water in place to mark them as visited.
    
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def bfs(row, col):
            q = deque([(row, col)])
            while q:
                r, c = q.popleft()
                for adj_r, adj_c in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
                    new_r = r + adj_r
                    new_c = c + adj_c

                    if 0 <= new_r < ROWS and 0 <= new_c < COLS and grid[new_r][new_c] == '1':
                        q.append((new_r, new_c))
                        grid[new_r][new_c] = '0'

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    grid[r][c] = '0'
                    islands += 1
                    bfs(r,c)
        
        return islands

# Testcases:
sol = Solution()
print(sol.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]) == 1)
print(sol.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]) == 3)