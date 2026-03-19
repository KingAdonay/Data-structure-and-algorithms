'''
    Time complexity: O(n * m)
    Space complexity: O(1)
'''
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        ROWS, COLS = len(board), len(board[0])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1)]
        c_row, c_col = click

        if board[c_row][c_col] == 'M':
            board[c_row][c_col] = 'X'
            return board

        def count_surrounding_mines(r: int, c:int) -> int:
            count = 0
            for i, j in directions:
                adj_r, adj_c = r+i, c+j
                if adj_r < 0 or adj_r == ROWS or adj_c < 0 or adj_c == COLS or board[adj_r][adj_c] != 'M':
                    continue

                count += 1

            return count

        def dfs(r: int, c:int) -> None:
            if r < 0 or r == ROWS or c < 0 or c == COLS or board[r][c] != 'E':
                return

            count = count_surrounding_mines(r,c)
            board[r][c] = 'B' if count == 0 else str(count)

            if board[r][c] == 'B':
                for i, j in directions:
                    dfs(r + i, c + j)

        dfs(c_row, c_col)
        return board
        