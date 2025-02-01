from collections import Counter

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        n = len(secret)
        bulls_count = 0
        cows_count = 0

        counter = Counter(secret)

        for i in range(n):
            if secret[i] == guess[i]:
                bulls_count += 1
                counter[secret[i]] -= 1
            
        for i in range(n):
            if secret[i] != guess[i] and guess[i] in counter and counter[guess[i]] > 0:
                cows_count += 1
                counter[guess[i]] -= 1

        
        return f"{bulls_count}A{cows_count}B"

# Tests A = bulls, B = cows
solution = Solution()
# Testcase 1: secret = "1807" guess = "7810"
hint = solution.getHint("1807", "7810")
print("1A3B" == hint)
# Testcase 1: secret = "1123" guess = "0111"
hint = solution.getHint("1123", "0111")
print("1A1B" == hint)
# Testcase 1: secret = "1122" guess = "1222"
hint = solution.getHint("1122", "1222")
print("3A0B" == hint)