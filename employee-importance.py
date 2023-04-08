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
        

        def dfs(employ):
            if not employ.subordinates:
                return employ.importance 

            

            tot = employ.importance
            for id in employ.subordinates:
                for emp in employees:
                    if id == emp.id:
                        tot += dfs(emp)
            return tot

        for em in employees:
            if em.id == id:
                return dfs(em)