# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxPath = root.val
        
        if not root:return 0
        
        def dfs(root):
            if not root:return 0
            
            leftSum = max(dfs(root.left),0)
            rightSum = max(dfs(root.right),0)
            
            self.maxPath = max(self.maxPath, leftSum + rightSum + root.val)
            
            return max(leftSum,rightSum)+root.val
        
        dfs(root)
        return self.maxPath
