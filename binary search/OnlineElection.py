from typing import List
from collections import defaultdict

'''
    911. Online Election
    
    Use binary search to find the top voted candidate at a given time t.
    
    Intuition:
    - We can maintain a dictionary to count the votes for each candidate and another dictionary to keep track of the leading candidate at each time point.
    - When we query for a time t, we can use binary search to find the largest time point that is less than or equal to t, and return the leading candidate at that time.
    
    Time Complexity: O(n) + O(log n) for the constructor since we iterate through the votes and maintain the leading candidate, O(n), and O(log n) for each query since we perform a binary search on the time points.
    Space Complexity: O(n) since we store the votes and leading candidates in dictionaries.
'''
class TopVotedCandidate:
    def __init__(self, persons: List[int], times: List[int]):
        self.votes = defaultdict(int)
        self.leaders = defaultdict(int)
        self.times = times

        maxx = (0, 0)
        for idx, person in enumerate(persons):
            self.votes[person] += 1
            if maxx[0] <= self.votes[person]:
                maxx = (self.votes[person], person)

            self.leaders[times[idx]] = maxx[1]


    def q(self, t: int) -> int:
        left, right = 0, len(self.times) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.times[mid] <= t:
                left = mid + 1
            else:
                right = mid - 1
        
        return self.leaders[self.times[right]]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)

# Testcases
# Testcase 1: persons = [0,1,1,0,0,1,0], times = [0,5,10,15,20,25,30], queries = [3,12,25,15] -> [0,1,1,0]
# Testcase 2: persons = [0,0,0,0,1], times = [0,6,39,52,75], queries = [45] -> [0]
# Testcase 3: persons = [0,1,1,0,0,1,0], times = [0,5,10,15,20,25,30], queries = [3],[12],[25],[15],[24],[8] -> [0,1,1,0,0,1]