from typing import List

'''
    1268. Search Suggestions System
    
    Use a Trie to store products and perform DFS to get suggestions.
    
    Use an array of children to represent each TrieNode for space efficiency and ordered traversal,
    since the output needs to be in lexicographical order.
    
    Time complexity:
    - Inserting all products: O(N * L) where N is the number of products and L is the average length of each product.
    - Searching suggestions for each character in searchWord: O(M * L) where M is the length of searchWord. Overall complexity: O(N * L + M * (L + 3))
    Space complexity: O(N * L) for storing the Trie.
'''
class TrieNode:
    def __init__(self, word: str = ""):
        self.children = [None] * 26
        self.word = word

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, product):
        cur = self.root
        for c in product:
            idx = ord(c) - ord('a')
            if not cur.children[idx]:
                cur.children[idx] = TrieNode()
            cur = cur.children[idx]
        cur.word = product 
    
    def search_suggestions(self, prefix: str, i: int, root: TrieNode | None) -> List[str]:

        def dfs(node: TrieNode | None, results: List[str]) -> None:
            if not node:
                return

            if len(results) == 3:
                return
            
            if node.word:
                results.append(node.word)
            
            for child in node.children:
                dfs(child, results)

        results = []
        cur = root
        if i == 0 and not root:
            cur = self.root
        elif not root:
            return [], None
        
        
        idx = ord(prefix[i]) - ord('a')
        cur = cur.children[idx]
        
        dfs(cur, results)

        return results, cur


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()

        for product in products:
            trie.insert(product)
        
        res = []
        lastNode = None
        for i in range(len(searchWord)):
            suggestions, node = trie.search_suggestions(searchWord, i, lastNode)
            lastNode = node
            res.append(suggestions)
        
        return res
        
# Example usage:
if __name__ == "__main__":
    solution = Solution()
    products = ["mobile","mouse","moneypot","monitor","mousepad"]
    searchWord = "mouse"
    print(solution.suggestedProducts(products, searchWord) == [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]])
    