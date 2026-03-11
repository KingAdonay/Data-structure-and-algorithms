
from typing import List

'''
    733. Flood Fill
    
    Use DFS to traverse the image starting from the given pixel.
    Change the color of the current pixel and recursively call DFS for its 4-directionally adjacent pixels.
    
    if the original color is the same as the new color, we can return the image immediately since no changes are needed.
    
    Time Complexity: O(N) where N is the number of pixels in the image
    Space Complexity: O(N) in the worst case when all pixels are connected and have the same color
'''

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS, COLS = len(image), len(image[0])
        original_color = image[sr][sc]
        
        if original_color == color:
            return image

        def dfs(row: int, col: int) -> None:
            if row < 0 or row == ROWS or col < 0 or col == COLS:
                return
            
            if image[row][col] != original_color:
                return
            
            image[row][col] = color

            for r, c in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                dfs(row + r, col + c)
        
        dfs(sr, sc)

        return image

# Testcases:
sol = Solution()
print(sol.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2) == [[2,2,2],[2,2,0],[2,0,1]])
print(sol.floodFill([[0,0,0],[0,0,0]], 0, 0, 2) == [[2,2,2],[2,2,2]])   