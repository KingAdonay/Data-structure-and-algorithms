from typing import List

# The solution is to finish traversing through the edges of the matrix and move inward by 1
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix), len(matrix[0])
        t, b = 0, n-1
        l, r = 0, m-1

        ans = []
        while t<=b and l<=r:
            for i in range(l, r+1):
                ans.append(matrix[t][i])

            for i in range(t+1, b+1):
                ans.append(matrix[i][r])
            
            if t != b:
                for i in range(r-1, l-1, -1):
                    ans.append(matrix[b][i])

            if l != r:
                for i in range(b-1, t, -1):
                    ans.append(matrix[i][l])

            t += 1
            b -= 1
            l += 1
            r -= 1

        return ans

# Tests
sol = Solution()
# Testcase 1: [[1,2,3],[4,5,6],[7,8,9]]
print([1,2,3,6,9,8,7,4,5] == sol.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
# Testcase 2: [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print([1,2,3,4,8,12,11,10,9,5,6,7] == sol.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
# Testcase 3: [[1,2,3]]
print([1,2,3] == sol.spiralOrder([[1,2,3]]))
# Testcase 4: [[1], [2], [3]]
print([1,2,3] == sol.spiralOrder([[1], [2], [3]]))
