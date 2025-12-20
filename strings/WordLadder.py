from collections import defaultdict, deque
from typing import List

'''
    127. Word Ladder
    
    Use BFS to find the shortest transformation sequence from beginWord to endWord.
    
    First build an adjacency dictionary where each key is a pattern with one letter of a word replaced by a wildcard '*',
    and the value is a list of words that match the pattern.
    This allows us to quickly find all words that can be reached by changing one letter.
    Use a queue to perform BFS starting from beginWord, and a set to track visited words.
    
    Keep track of the number of levels (transformations) in the BFS we have performed to find the shortest path.
    
    Time complexity: O(N * M^2), where N is the number of words in the wordList and M is the length of each word.
    Space complexity: O(N * M), for storing the adjacency list.
'''
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        wordList.append(beginWord)
        adj = defaultdict(list)
        
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                adj[pattern].append(word)
        
        q = deque([beginWord])
        visited = set([beginWord])
        res = 1 # count is one because count includes search word

        while q:
            for i in range(len(q)): # when loop finishes, it means we have finished processing the current level 
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + '*' + word[j+1:]
                    for neighbour in adj[pattern]:
                        if neighbour not in visited:
                            visited.add(neighbour)
                            q.append(neighbour)

            res += 1 # increment the level (depth)

        return 0
    
# Testcases:
sol = Solution()
print(sol.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]) == 5)
print(sol.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]) == 0)
print(sol.ladderLength("a", "c", ["a","b","c"]) == 2)