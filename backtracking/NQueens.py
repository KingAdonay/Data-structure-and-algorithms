from collections import defaultdict
from typing import List

'''
    51. N-Queens
    
    Solution using Backtracking
    
    Intuition: 
    Place queens row by row, checking for validity at each step.
    If a row cannot have a queen placed in any column, backtrack to the previous row and try the next column.
    
    Approach:
    1. Create is_valid function to check if a queen can be placed at a given position.
    2. Define a backtracking function that attempts to place queens row by row.
    3. For each row, try placing a queen in each column and check if it's valid.
    4. If valid, place the queen and recursively attempt to place queens in the next row.
    5. If all queens are placed, add the board configuration to the results.
    6. If no column is valid, backtrack to the previous row and try the next column.
    
    Time complexity: O(N * N!)
    Space complexity: O(N^2) for the board
'''
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        row_set = defaultdict(set)
        col_set = defaultdict(set)

        def is_valid(board, r, c):
            if 'Q' in row_set[r]:
                return False
            
            if 'Q' in col_set[c]:
                return False
            
            i, j = r, c
            while i > 0 and j > 0:
                if board[i-1][j-1] == 'Q':
                    return False
                i -= 1
                j -= 1
            
            i, j = r, c
            while i > 0 and j < n - 1:
                if board[i-1][j+1] == 'Q':
                    return False
                i -= 1
                j += 1
            
            i, j = r, c
            while i < n - 1 and j < n - 1:
                if board[i+1][j+1] == 'Q':
                    return False
                i += 1
                j += 1
          
            i, j = r, c
            while i < n - 1 and j > 0:
                if board[i+1][j-1] == 'Q':
                    return False
                i += 1
                j -= 1

            return True
        
        def backtrack(board, r):
            if r == n:
                ans = [''] * n
                for i, row in enumerate(board):
                    ans[i] = ''.join(row)
                res.append(ans)
                return 

            
            for j in range(n):
                if is_valid(board, r, j):
                    row_set[r].add('Q')
                    col_set[j].add('Q')
                    board[r][j] = 'Q'
                    
                    backtrack(board, r+1)
                    
                    board[r][j] = '.'
                    row_set[r].remove('Q')
                    col_set[j].remove('Q')
                    
        
        backtrack([['.'] * n for i in range(n)], 0)

        return res


