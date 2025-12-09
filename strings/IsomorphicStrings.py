
'''
    Use two hash maps to store the mapping from characters in s to characters in t and vice versa.
    Iterate through the characters of both strings simultaneously.
    For each pair of characters (s[i], t[i]):
        - If s[i] is already mapped to a character in t, check if it matches t[i]. If not, return False.
        - If t[i] is already mapped to a character in s, check if it matches s[i]. If not, return False.
        - If neither character is mapped, create the mapping in both hash maps.
    If we complete the iteration without conflicts, return True.
    
    Time complexity: O(N) where N is the length of the first string.
    Space complexity: O(N + M) where N and M are the number of unique characters in s and t respectively.
'''

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


# Testcases:
sol = Solution()
print(sol.isIsomorphic("egg", "add") == True)  # Output: True
print(sol.isIsomorphic("foo", "bar") == False)  # Output: False
print(sol.isIsomorphic("paper", "title") == True)  # Output: True
print(sol.isIsomorphic("badc", "baba") == False) # Output: False