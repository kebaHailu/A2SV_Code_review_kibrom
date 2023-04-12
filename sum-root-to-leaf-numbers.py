# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def convert(root,path=""):
            nonlocal ans
            if not root:
                return 
            path += str(root.val)
            convert(root.left,path)
            convert(root.right,path)

            if root.left == None and root.right == None:
                ans += int(path)
            
        
        convert(root)
        return ans