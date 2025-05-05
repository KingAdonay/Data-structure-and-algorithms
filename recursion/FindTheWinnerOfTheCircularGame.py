class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = []
        for i in range(n):
            friends.append(i + 1)
        
        def helper(frds: list, idx)->list:
            if len(frds) == 1:
                return frds

            i = idx + k - 1
            while i >= len(frds):
                i -= len(frds)
            
            arr = frds[:i] + frds[i+1:]
            
            return helper(arr, i)

            
        ans = helper(friends, 0)
        
        return ans[0]
            
# Tests
sol = Solution()
# Testcase 1:
n = 5
k = 2
expected = 3
print(expected == sol.findTheWinner(n, k))
# Testcase 2:
n = 6
k = 5
expected = 1
print(expected == sol.findTheWinner(n, k))