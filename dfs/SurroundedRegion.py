
from typing import List


''' 
    130. Surrounded Regions
    
    Use DFS to mark all 'O's connected to the borders as '#'.
    Then, iterate through the board and flip all remaining 'O's to 'X's and '#' back to 'O's.
    
    Time Complexity: O(ROWS * COLS) since we may visit each cell at most once
    Space Complexity: O(ROWS * COLS) in the worst case if the grid is filled with 'O's
'''

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])

        def dfs(row: int, col: int) -> None:
            if row < 0 or row == ROWS or col < 0 or col == COLS or board[row][col] != 'O':
                return
            
            board[row][col] = '#'

            for i, j in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                dfs(row+i, col+j)
        
        for row in range(ROWS):
            dfs(row, 0)
            dfs(row, COLS - 1)
        
        for col in range(COLS):
            dfs(0, col)
            dfs(ROWS-1, col)
        
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == '#':
                    board[row][col] = 'O'
                    
                    
# Testcases:
sol = Solution()
# Testcase 1
board1 = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
sol.solve(board1)
print(board1 == [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]])  
# Testcase 2
board2 = [["O","O"],["O","O"]]
sol.solve(board2)
print(board2 == [["O","O"],["O","O"]])