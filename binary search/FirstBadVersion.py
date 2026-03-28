'''
    278. First Bad Version
    
    Using binary search, we can efficiently find the first bad version. We start with two pointers, 
    `left` and `right`, initialized to 1 and `n` respectively. We calculate the midpoint `mid` and check 
    if it is a bad version using the provided `isBadVersion` API.
    
    If `mid` is not a bad version, it means the first bad version must be to the right of `mid`, so we move the `left` pointer to `mid + 1`.
    If `mid` is a bad version, it means the first bad version is at `mid` or to the left of `mid`, so we move the `right` pointer to `mid`.
    
    We continue this process until `left` is equal to `right`, at which point `left` (or `right`) will be pointing to the first bad version.
    
    Time Complexity: O(log N) due to the binary search
    Space Complexity: O(1) since we are using only a constant amount of space
'''

def isBadVersion(version: int) -> bool:
    if version >= 4:
        return True
    return False

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n

        while left < right:
            mid = (left + right) // 2
            if not isBadVersion(mid):
                left = mid + 1
            else:
                right = mid

        return left
        
# Testcases
sol = Solution()
# Testcase 1: n = 5 -> 4
n1 = 5
print(sol.firstBadVersion(n1) == 4)