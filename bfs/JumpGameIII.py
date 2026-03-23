
from typing import List
from collections import deque

'''    
    1306. Jump Game III
    
    Use BFS to explore all possible jumps from the starting index, and keep track of visited indices to avoid cycles.
    
    Time Complexity: O(N) since we visit each index at most once
    Space Complexity: O(N) in the worst case if we have to visit all indices, otherwise O(W) where W is the maximum width of the search tree
'''

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q, visited = deque([start]), set()

        while q:
            cur_idx = q.popleft()
            visited.add(cur_idx)
            if arr[cur_idx] == 0:
                return True

            left, right = cur_idx - arr[cur_idx], cur_idx + arr[cur_idx]
            
            if left >= 0 and left not in visited:
                q.append(left)
            if right < len(arr) and right not in visited:
                q.append(right)
        
        return False

# Testcases
sol = Solution()
# Testcase 1: arr = [4,2,3,0,3,1,2], start = 5 -> True
arr1 = [4,2,3,0,3,1,2]
start1 = 5
print(sol.canReach(arr1, start1) == True)
# Testcase 2: arr = [   4,2,3,0,3,1,2], start = 0 -> True
arr2 = [4,2,3,0,3,1,2]
start2 = 0
print(sol.canReach(arr2, start2) == True)
# Testcase 3: arr = [3,0,2,1,2], start = 2 -> False
arr3 = [3,0,2,1,2]
start3 = 2
print(sol.canReach(arr3, start3) == False)