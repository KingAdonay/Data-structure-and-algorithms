from collections import defaultdict
from typing import List

'''
    37. Sudoku Solver
    
    Intuition:
    Use backtracking to fill the board cell by cell, checking for validity at each step.
    If a cell cannot be filled with any valid number, backtrack to the previous cell and try the next number.
    
    Approach:
    1. Create sets to track valid numbers for each row, column, and 3x3 box.
    2. Define a backtracking function that attempts to fill the board.
    3. For each empty cell, try placing numbers 1-9 and check if they are valid.
    4. If valid, place the number and recursively attempt to fill the next cell.
    5. If the board is completely filled, return True. If no number is valid, backtrack.
    
    Time complexity: O(9^(m*n)) where m and n are the dimensions of the board (9x9)
    Space complexity: O(m*n) for the recursion stack and sets   
'''

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        valid_rows = defaultdict(set)
        valid_cols = defaultdict(set)
        valid_boxes = defaultdict(set)

        def is_valid(r, c, val):
            if val in valid_rows[r] or val in valid_cols[c] or val in valid_boxes[(r // 3), (c // 3)]:
                return False
            
            return True
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val != '.':
                    valid_rows[r].add(val)
                    valid_cols[c].add(val)
                    valid_boxes[(r//3, c//3)].add(val)
        
        def backtrack(r,c):
            if r == 9:
                return True
            
            next_r = r + (c+1) // 9
            next_c = (c+1) % 9
            
            if board[r][c] != '.':
                return backtrack(next_r, next_c)
            
            for num in '123456789':
                if is_valid(r, c, str(num)):
                    valid_rows[r].add(num)
                    valid_cols[c].add(num)
                    valid_boxes[(r // 3, c // 3)].add(num)
                    
                    board[r][c] = num

                    if backtrack(next_r, next_c):
                        return True
                    
                    board[r][c] = '.'
                    valid_rows[r].remove(num)
                    valid_cols[c].remove(num)
                    valid_boxes[(r // 3, c // 3)].remove(num)
            
            return False

        backtrack(0,0)

# Testcases:
sol = Solution()
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
ans = [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
sol.solveSudoku(board)
print(board == ans)