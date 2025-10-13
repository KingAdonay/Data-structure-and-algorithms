import collections
from typing import List


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        recipes_set = set(recipes)
    
        in_degree = collections.defaultdict(int)
        neighbours = collections.defaultdict(set)
        queue = collections.deque([])
        ans = []

        for supply in supplies:
            in_degree[supply] = 0

        for i in range(len(ingredients)):
            for ingredient in ingredients[i]:
                in_degree[recipes[i]] += 1
                neighbours[ingredient].add(recipes[i])

        for key, value in in_degree.items():
            if value == 0:
                queue.append(key)
        
        while queue:
            key = queue.popleft()
            if key in recipes_set:
                ans.append(key)
            
            for neighbour in neighbours[key]:
                in_degree[neighbour] -= 1
                if in_degree[neighbour] == 0:
                    queue.append(neighbour)
        
        return ans
                


# Tests
sol = Solution()

# Testcase 1: recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast","flour","corn"]
print(sol.findAllRecipes(["bread"], [["yeast","flour"]], ["yeast","flour","corn"]) == ["bread"])
# Testcase 2: recipes = ["bread","sandwich"], ingredients = [["yeast","flour"],["bread","meat"]], supplies = ["yeast","flour","meat"]
print(sol.findAllRecipes(["bread","sandwich"], [["yeast","flour"],["bread","meat"]], ["yeast","flour","meat"]) == ["bread","sandwich"])
# Testcase 3: recipes = ["bread","sandwich","burger"], ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], supplies = ["yeast","flour","meat"]
print(sol.findAllRecipes(["bread","sandwich","burger"], [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], ["yeast","flour","meat"]) == ["bread","sandwich","burger"])