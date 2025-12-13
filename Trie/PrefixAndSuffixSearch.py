from typing import List

'''
    745. Prefix and Suffix Search
    
    Use a Trie to store prefixes and suffixes (in reversed order) of words. Each TrieNode maintains sets of word indices for prefixes and suffixes.
    To find the maximum index of a word with a given prefix and suffix, find the nodes for both prefix and suffix (reversed) values,
    intersect the sets from the prefix and suffix tries and find the maximum index, if not found return -1.
    
    Time Complexity: O(P + S + N) for each query, where P is the length of the prefix and S is the length of the suffix.
    Space Complexity: O(N * L) where N is the number of words and L is the average length of the words.

'''
class TrieNode:
    def __init__(self):
        self.children = {}
        self.prefix_set = set()
        self.suffix_set = set()

class Dictionary:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word: str, word_idx: int) -> None:
        cur = self.root
        word_size = len(word)
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            cur.prefix_set.add(word_idx)
        
        cur = self.root
        for i in range(word_size - 1, -1, -1):
            c = word[i]
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            cur.suffix_set.add(word_idx)
        
    def find(self, prefix: str, suffix: str) -> set | None:
        i, p, cur_p = 0, len(prefix), self.root
        j, s, cur_s = 0, len(suffix), self.root
        
        while i < p:
            if prefix[i] not in cur_p.children:
                return None
            cur_p = cur_p.children[prefix[i]]
            
            i += 1
        
        while j < s:
            if suffix[j] not in cur_s.children:
                return None
            cur_s = cur_s.children[suffix[j]]
            
            j += 1
        
        return cur_p.prefix_set.intersection(cur_s.suffix_set)

class WordFilter:

    def __init__(self, words: List[str]):
        self.dictionary = Dictionary()
        self.cache = {}

        for i, word in enumerate(words):
            self.dictionary.add(word, i)
    
    def f(self, pref: str, suff: str) -> int:
        key = (pref, suff)
    
        if key in self.cache:
            return self.cache[key]
        
        sett = self.dictionary.find(pref, suff[::-1])

        self.cache[key] = max(sett) if sett else -1 # max index
        
        return self.cache[key]


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)

# Testcases
wordFilter = WordFilter(["apple", "banana", "appetite"])
print(wordFilter.f("app", "le") == 0)  # Output:
print(wordFilter.f("ban", "na") == 1)  # Output: 1
print(wordFilter.f("app", "ite") == 2)  # Output: 2
print(wordFilter.f("a", "e") == 2)  # Output: 2
print(wordFilter.f("b", "a") == 1)  # Output: 1
print(wordFilter.f("x", "y") == -1)  # Output: -1