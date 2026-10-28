# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.recurse(root, 0)
        
        

    def recurse(self, root, cur_max):
        if root:
            cur = self.maxDepth(root.left) + self.maxDepth(root.right)
            cur_max = max(cur_max, cur)
        else:
            return cur_max
        ret_max = max(self.recurse(root.left, cur_max), self.recurse(root.right, cur_max))
        return ret_max

    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return 1 + max(left_depth, right_depth)
        