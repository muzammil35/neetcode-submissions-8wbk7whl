# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root and not root.left and not root.right:
            return True
        if not root:
            return True
        left_height = self.depth(root.left)
        right_height = self.depth(root.right)
        if abs(left_height - right_height) <=1:
            is_left_balanced = self.isBalanced(root.left)
            is_right_balanced = self.isBalanced(root.right)
            return is_left_balanced and is_right_balanced
        else:
            return False
        
            
        
        

        


    def depth(self, root):
        if root:
            left_sub_depth = 1 + self.depth(root.left)
            right_sub_depth = 1 + self.depth(root.right)
            return max(left_sub_depth, right_sub_depth)
        else:
            return 0


        