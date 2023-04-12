# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''
        
        st = str(root.val)
        st_l ='('+self.tree2str(root.left)+')' if root.left else ''
        st_r = '('+self.tree2str(root.right)+')' if root.right else ''
        
        if st_l == '' and st_r != '':
            st_l = '()'
        return st + st_l + st_r