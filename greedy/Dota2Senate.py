from collections import deque 


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        d_queue = deque()
        r_queue = deque()

        for i, p in enumerate(senate):
            if p == 'R':
                r_queue.append(i)
            else:
                d_queue.append(i)
        
        while d_queue and r_queue:
            d = d_queue.popleft()
            r = r_queue.popleft()
            if d < r:
                d_queue.append(d + len(senate))
            else:
                r_queue.append(r + len(senate))
        
        return 'Radiant' if r_queue else 'Dire'

# Tests
sol = Solution()
# Testcase 1: "RD" -> "Radiant"
print(sol.predictPartyVictory("RD") == "Radiant")
# Testcase 2: "RDD" -> "Dire"
print(sol.predictPartyVictory("RDD") == "Dire")
# Testcase 3: "RRDD" -> "Radiant"
print(sol.predictPartyVictory("RRDD") == "Radiant")
# Testcase 4: "D" -> "Dire"
print(sol.predictPartyVictory("D") == "Dire")
# Testcase 5: "DRDRR" -> "Dire"
print(sol.predictPartyVictory("DRDRR") == "Dire")