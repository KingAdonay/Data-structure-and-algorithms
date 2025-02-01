class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)
        mapp_t = {}
        mapp_s = {}
        for i in range(n):
            if t[i] in mapp_t:
                if mapp_t[t[i]] != s[i]:
                    return False
            else:
                if s[i] in mapp_s and mapp_s[s[i]] != t[i]:
                    return False

                mapp_s[s[i]] = t[i]
                mapp_t[t[i]] = s[i]
        
        return True

# Tests
solution = Solution()
# Testcase 1: "foo" "bar"
print(False == solution.isIsomorphic("foo", "bar"))
# Testcase 2: "egg" "add"
print(True == solution.isIsomorphic("egg", "add"))
# Testcase 3: "paper" "title"
print(True == solution.isIsomorphic("paper", "title"))
# Testcase 4: "bbbaaaba" "aaabbbba"
print(False == solution.isIsomorphic("bbbaaaba", "aaabbbba"))
