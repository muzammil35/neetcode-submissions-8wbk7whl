# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if root: 
            same = self.isSame(root, subRoot)
            if same:
                return True
            else:
                isLeft = self.isSubtree(root.left, subRoot)
                isRight = self.isSubtree(root.right, subRoot)
                return isLeft or isRight
        else:
            return False


    def isSame(self, a, b):
        if not a and not b:
            return True
        if not a and b:
            return False
        if not b and a:
            return False

        if a.val == b.val:
            left = self.isSame(a.left, b.left)
            right = self.isSame(a.right, b.right)
            return left and right
        else:
            return False
        