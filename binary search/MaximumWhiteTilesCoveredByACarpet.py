from typing import List

'''
    2271. Maximum White Tiles Covered by a Carpet
    
    Solution using Binary Search
    
    Time complexity: O(N log N)
    Space complexity: O(N)
'''

class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort(key = lambda x: x[0])
        ans = 0
        n = len(tiles)
        prefix = [0] * n
        for i in range(n):
            prefix[i] = tiles[i][1] - tiles[i][0] + 1
            if i > 0:
                prefix[i] += prefix[i - 1]
        
        for i in range(n):
            start, end = tiles[i]
            expected_end = start + carpetLen - 1
            if end > expected_end:
                return carpetLen

            left, right = i, i - 1 # fully covered tiles start and end idx
            
            # binary search for the last fully covered tile group and use that as
            # the right boundary
            l, r = i, n - 1
            while l <= r:
                mid = (l + r) // 2
                if tiles[mid][1] <= expected_end:
                    right = mid
                    l = mid + 1
                else:
                    r = mid - 1
            
            cur = 0
            if right != i-1:
                cur += prefix[right]
                if left > 0:
                    cur -= prefix[left - 1]
                    print(cur)
            
            # add partially covered tiles if available
            if right + 1 < n:
                cur += max(0, expected_end - tiles[right + 1][0] + 1)
            
            ans = max(ans, cur)

        return ans