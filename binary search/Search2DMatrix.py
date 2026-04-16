class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        left, right = 0, (ROWS * COLS) - 1
        while left <= right:
            mid = (left + right) // 2
            row, col = mid // COLS, mid % COLS
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1


        return False
                
'''
Testcase
[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
3 -> TRUE
[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
13 -> FALSE
[[1]]
2 -> FALSE
'''