from typing import List

'''
    1233. Remove Sub-Folders from the Filesystem
    
    Use a Trie to store folder paths and mark the end of main folders.
    Ignore inserting sub-folders if a parent folder is already marked as a main folder.
    Use prefix dfs traversal to collect only main folders.
    
    Time complexity:
    - Inserting all folders: O(N * L) where N is the number of folders and L is the average length of each folder path.
    - Collecting main folders: O(N * L) in the worst case where all folders are main folders.
    Overall complexity: O(N * L)
    Space complexity: O(N * L) for storing the Trie. 
'''
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_folder = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, folder:str) -> None:
        cur = self.root
        l = len(folder)
        w = ''
        for i in range(l):
            if cur.is_folder:
                return
                
            w += folder[i] if folder[i] != '/' else ''
            if (folder[i] == '/' or i == l-1) and w:
                if w not in cur.children:
                    cur.children[w] = TrieNode()
                
                cur = cur.children[w]
                w=''
        cur.is_folder = True
    
    def get_main_folders(self) -> List[str]:
        results = []

        def dfs_helper(node: TrieNode, folder: str, results: List[str]) -> None:
            if node.is_folder:
                results.append(folder)
                return
            
            for key, child in node.children.items():
                dfs_helper(child, folder + '/' + key, results)
        
        dfs_helper(self.root, '', results)
        return results

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()
        for f in folder:
            trie.insert(f)
        
        return trie.get_main_folders()


sol = Solution()
print(sol.removeSubfolders(["/a","/a/b","/c/d","/c/d/e","/c/f"]) == ["/a","/c/d","/c/f"])  # ["/a","/c/d","/c/f"]
print(sol.removeSubfolders(["/a","/a/b/c","/a/b/d"]) == ["/a"])