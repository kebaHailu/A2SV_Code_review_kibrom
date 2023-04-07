# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        path_sum = {0:1}
        count = 0

        def dfs(root,cur_sum):
            nonlocal count 

            if not root:
                return 
            
            cur_sum += root.val 
            count += path_sum.get(cur_sum-targetSum,0)
            path_sum[cur_sum] = path_sum.get(cur_sum,0)+1

            dfs(root.left,cur_sum)
            dfs(root.right,cur_sum)
            
            path_sum[cur_sum] -= 1
        
        dfs(root,0)
        return count