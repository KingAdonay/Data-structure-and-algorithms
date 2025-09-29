class Solution:
    def countVowels(self, word: str) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        n = len(word)

        count = 0
        for i, c in enumerate(word):
            if c in vowels:
                count += (i + 1) * (n - i) # number of substrings that include c

        return count
    
# Tests
sol = Solution()
# Testcase 1: "aba"
print(sol.countVowels("aba") == 6)
# Testcase 2: "abc"
print(sol.countVowels("abc") == 3)  