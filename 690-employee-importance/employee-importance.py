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
        graph = {}
        importance = {}
        for e in employees:
            graph[e.id]=e.subordinates
            importance[e.id]=e.importance

        total = 0
        def dfs(current,seen):
            nonlocal total
            seen.add(current)
            total += importance[current]

            for subordinates in graph[current]:
                dfs(subordinates,seen)

        dfs(id,set())
        return total

