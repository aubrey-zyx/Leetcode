"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

# BFS
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        mp = {employee.id: employee for employee in employees}
        total = 0
        q = collections.deque([id])
        while q:
            cur_id = q.popleft()
            employee = mp[cur_id]
            total += employee.importance
            for sub_id in employee.subordinates:
                q.append(sub_id)
        return total


# DFS BFS
class Solution2:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        mp = {employee.id: employee for employee in employees}

        def dfs(id: int) -> int:
            employee = mp[id]
            return employee.importance + sum(dfs(sub_id) for sub_id in employee.subordinates)

        return dfs(id)