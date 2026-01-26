
from typing import List

'''
    304. Range Sum Query 2D - Immutable

    Intuition:
    To efficiently calculate the sum of elements in a submatrix defined by its upper left and lower right corners,
    we can use a prefix sum matrix. This allows us to compute the sum in constant time after an initial preprocessing step.

    Approach:
    1. Preprocessing Step:
       - Create a prefix sum matrix where each element at (i, j) contains the sum of all elements from the original matrix
         from (0, 0) to (i-1, j-1).
       - This is done by iterating through each element of the original matrix and updating the prefix sum matrix accordingly.

    2. Query Step:
       - To find the sum of elements in the submatrix defined by (row1, col1) and (row2, col2),
         we can use the prefix sums to calculate it in constant time using the formula:
         sumRegion = pre[row2 + 1][col2 + 1] - pre[row1][col2 + 1] - pre[row2 + 1][col1] + pre[row1][col1]

    Time complexity:
    - Preprocessing: O(m * n), where m and n are the dimensions of the matrix.
    - Query: O(1) for each sumRegion call.

    Space complexity:
    - O(m * n) for storing the prefix sum matrix.
'''

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            self.pre = [[0]]
            return

        m, n = len(matrix), len(matrix[0])
        self.pre = [[0] * (n + 1) for _ in range(m + 1)]

        for r in range(m):
            row_sum = 0
            for c in range(n):
                row_sum += matrix[r][c]
                self.pre[r + 1][c + 1] = self.pre[r][c + 1] + row_sum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        pre = self.pre
        return (pre[row2 + 1][col2 + 1]
                - pre[row1][col2 + 1]
                - pre[row2 + 1][col1]
                + pre[row1][col1])


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

# Testcases:
if __name__ == "__main__":
    matrix = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5]
    ]
    numMatrix = NumMatrix(matrix)
    assert numMatrix.sumRegion(2, 1, 4, 3) == 8
    assert numMatrix.sumRegion(1, 1, 2, 2) == 11
    assert numMatrix.sumRegion(1, 2, 2, 4) == 12