from collections import Counter, deque
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        freq = deque(sorted(counter, key=lambda x:counter[x], reverse=True))
        
        ans = []
        i = 0
        while freq:
            if counter[freq[0]] > 0:
                ans.append(freq[0])
                counter[freq[0]] -= 1
                
                left = 1
                right = len(freq) - 1
                idle_count = n
                
                while left<=right and idle_count > 0 and counter[freq[0]] > 0:
                    if counter[freq[left]] > 0:
                        ans.append(freq[left])
                        counter[freq[left]] -= 1
                        idle_count -= 1
                        left += 1
                    elif counter[freq[right]] > 0:
                        ans.append(freq[right])
                        counter[freq[right]] -= 1
                        idle_count -= 1
                        right -= 1
                    else:
                        left += 1                     
                        
                while idle_count > 0 and counter[freq[0]] > 0:
                    ans.append('idle')
                    idle_count -= 1    
                    
            if counter[freq[0]] == 0:
                freq.popleft()
            
            freq = deque(sorted(freq, key=lambda x:counter[x], reverse=True))
            
        return len(ans)
        

# Tests
sol = Solution()
# Testcase 1; ["A","A","A","B","B","B"] n = 2 output = 8
# Testcase 2; ["A","A","A","B","B","B"] n = 3 output = 10
# Testcase 3; ["A","A","A","B","B","B", "C"] n = 3 output = 10
# Testcase 4; ["A","A","A","B","B","B", "C","C","C", "D", "D", "E"] n = 2 output = 12
# Testcase 5; ["A","B","C","A"] n = 100 output = 102
# Testcase 6; ["C"] n = 3 output = 1
# Testcase 7; ["B","C","D","A","A","A","A","G"] n = 1 output = 8
# Testcase 8; [["A","B","C","D","A","B","V"] n = 3 output = 7
ans = sol.leastInterval(["A","B","C","D","A","B","V"], 3)
print(ans == 7)
        