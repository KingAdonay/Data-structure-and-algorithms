from functools import cmp_to_key
from collections import defaultdict
from typing import List

'''
692. Top K Frequent Words

Use a trie to store the words and a hashmap to count their frequencies.

Sort the words based on their frequencies and lexicographical order to get the top k frequent words.

Time complexity: O(N log N + K), where N is the number of unique words.
Space complexity: O(N) for the trie and hashmap.
'''

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            
            curr = curr.children[c]
        curr.is_word = True
    
    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            
            curr = curr.children[c]
        
        return curr.is_word

def compare(a, b) -> bool:
    if a[1] == b[1]:
        if a[0] < b[0]:
            return -1
        else:
            return 1
    return b[1] - a[1]

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        frequency = defaultdict(int)
        for word in words:
            if trie.search(word):
                frequency[word] += 1
        
        tuple_list = list(frequency.items())
        tuple_list.sort(key = cmp_to_key(compare))

        return [tuple_list[i][0] for i in range(k)]


'''
Heap solution (O(N log K) time, O(N) space)
'''
import heapq

class HeapItem:
    def __init__(self, word: str, freq: int):
        self.word = word
        self.freq = freq
    
    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word
        return self.freq < other.freq
    
class SolutionHeap:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        frequency = defaultdict(int)
        for word in words:
            frequency[word] += 1
        
        min_heap = []
        for word, freq in frequency.items():
            heapq.heappush(min_heap, HeapItem(word, freq))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        result = []
        while min_heap:
            result.append(heapq.heappop(min_heap).word)
        
        return result[::-1]


# Testcases:
s = Solution()
sh = SolutionHeap()

print(s.topKFrequent(["i","love","leetcode","i","love","coding"], 2) == ["i","love"]) # ["i","love"]
print(s.topKFrequent(["the","day","is","sunny","the","the","the","sunny","is","is"], 4) == ["the","is","sunny","day"]) # ["the","is","sunny","day"]
print(sh.topKFrequent(["i","love","leetcode","i","love","coding"], 2) == ["i","love"]) # ["i","love"]
print(sh.topKFrequent(["the","day","is","sunny","the","the","the","sunny","is","is"], 4) == ["the","is","sunny","day"]) # ["the","is","sunny","day"]