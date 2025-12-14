'''
    71. Simplify Path
    
    Split the given path by '/'  to get the individual directory components.
    Use a stack to process each component:
        - If the component is '..', pop from the stack if it's not empty (move up one directory).
        - If the component is '.' or an empty string, do nothing (stay in the current directory).
        - Otherwise, push the component onto the stack (move into the directory).
    Finally, join the components in the stack with '/' and prepend a '/' to form the simplified path.
    
    Space Complexity: O(n) in the worst case, where n is the length of the input path.
    Time Complexity: O(n), where n is the length of the input path.
'''


class Solution:
    def simplifyPath(self, path: str) -> str:
        directories = path.split('/')
        
        stack = []
        for directory in directories:
            if directory == '..' and stack:
                stack.pop()
            elif directory and directory != '.' and directory != '..':
                stack.append(directory)
        
        return '/' + '/'.join(stack) 

# Testcases:
sol = Solution()
print(sol.simplifyPath("/home/") == "/home") # Output: "/home"
print(sol.simplifyPath("/../") == "/") # Output: "/"
print(sol.simplifyPath("/home//foo/") == "/home/foo") # Output: "/home/foo"
print(sol.simplifyPath("/a/./b/../../c/") == "/c") # Output: "/c"
print(sol.simplifyPath("/a/../../b/../c//.") == "/c") # Output: "/c"
print(sol.simplifyPath("/a//b////c/d//././/..") == "/a/b/c") # Output: "/a/b/c"