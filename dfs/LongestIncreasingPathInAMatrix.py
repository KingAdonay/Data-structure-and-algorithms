from typing import List

'''
    329. Longest Increasing Path in a Matrix
    
    Intuition:
    For every position in the matrix we need to travel in four directions to find the LIP count, and retain the maximum value.
    To explore the matrix we can use DFS to start from one position and continue until the LIP is invalid or we are out of bound.
    
    To make the solution efficient, we can add a cache matrix to remember the already explored positions LIP count. 
    
    Approach:
    1. Create a dp array to cache the LIP count for all positions in the matrix.
    2. Define a dfs helper function to find the maximum LIP for a position.
    3. Call the dfs method for every position in the matrix.
    4.  4.1. The dfs method should check the validitiy of the positions and the LIP property.
        4.2. Check if a value for a position is already in the dp cache, return if it exists.
        4.2. Take the maximum out of all four routes, add it to 1, the current position, and update the cache, and return the LIP count.
    5. Keep track of the maximum count of the LIP on every iteration and return the maximum value.
    
    Complexity:
    Time: O(m * n)
    Space: O(m * n)
'''

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for i in range(m)]

        def dfs(r, c, prev):
            if r == m or c == n or r == -1 or c == -1:
                return 0

            if matrix[r][c] <= prev:
                return 0

            if dp[r][c] != 0:
                return dp[r][c]

            dp[r][c] = 1 + max(
                dfs(r - 1, c, matrix[r][c]),
                dfs(r, c + 1, matrix[r][c]),
                dfs(r + 1, c, matrix[r][c]),
                dfs(r, c - 1, matrix[r][c]),
            )

            return dp[r][c]

        res = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                res = max(res, dfs(r, c, -1))

        return res

# Tests
sol = Solution()
# Testcase 1:
matrix = [[9,9,4],[6,6,8],[2,1,1]]
print(sol.longestIncreasingPath(matrix) == 4)
# Testcase 2:
matrix = [[3,4,5],[3,2,6],[2,2,1]]
print(sol.longestIncreasingPath(matrix) == 4)
# Testcase 3:
matrix = [[1]]
print(sol.longestIncreasingPath(matrix) == 1)
# Testcase 4:
matrix = [[0,9,7,0],[7,4,1,9],[2,6,1,3],[8,0,9,9]]
print(sol.longestIncreasingPath(matrix) == 3)