class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}
        
        def dfs(i, j):
            if i >= len(s) and j >= len(p):
                return True
            
            if j >= len(p):
                return False

            tup = (i, j)
            if tup in cache:
                return cache[tup]
            
            matched = i < len(s) and (s[i] == p[j] or p[j] == '.')
            # string could contain * or not
            if j + 1 < len(p) and p[j + 1] == '*':
                # either use the * or skip it
                cache[tup] = (matched and dfs(i + 1, j)) or dfs(i, j + 2)
                return cache[tup]
            
            if matched:
                cache[tup] = dfs(i+1, j+1)
                return cache[tup]
            
            cache[tup] = False
            return cache[tup]
        
        return dfs(0,0)

# Tests
sol = Solution()
# Testcase 1: s = "aa", p = "a"
print(sol.isMatch("aa", "a") == False)
# Testcase 2: s = "aa", p = "a*"
print(sol.isMatch("aa", "a*") == True)
# Testcase 3: s = "ab", p = ".*"
print(sol.isMatch("ab", ".*") == True)
# Testcase 4: s = "aab", p = "c*a*b"
print(sol.isMatch("aab", "c*a*b") == True)