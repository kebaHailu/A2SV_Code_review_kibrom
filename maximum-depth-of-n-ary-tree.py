"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0 
        def dfs(root):
            if not root:
                return 1 
            
            cur_max = 0
            for child in root.children:
                cur_max = max(cur_max,dfs(child))
            
            return cur_max + 1 

        return dfs(root)