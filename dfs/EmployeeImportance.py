"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        adj = { employee.id: employee for employee in employees }

        def dfs(id:int) -> int:
            if id not in adj:
                return 0

            sub_sum = 0
            for sub_id in adj[id].subordinates:
                sub_sum += dfs(sub_id)

            return adj[id].importance + sub_sum

        return dfs(id)