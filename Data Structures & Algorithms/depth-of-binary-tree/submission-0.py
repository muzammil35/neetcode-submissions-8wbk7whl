# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        res = self.recurse(root, 1)
        return res

    def recurse(self, node, depth):
        if node.left == None and node.right == None:
            return depth
        else:
            left_depth = depth
            right_depth = depth
            
            if node.left:
                left_depth = self.recurse(node.left, depth+1)
            if node.right:
                right_depth = self.recurse(node.right, depth+1)
        return max(left_depth, right_depth)

