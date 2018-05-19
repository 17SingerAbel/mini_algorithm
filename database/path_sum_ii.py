# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
        	return []
        lst = []
        if not root.left and not root.right and root.val == sum:
        	return [[root.val]]
        left = self.pathSum(root.left, sum-root.val)
        right = self.pathSum(root.right, sum-root.val)
        
        if left:
            for i in left:
                i.insert(0, root.val)
            lst += left
        if right:
            for j in right:
                j.insert(0, root.val)
            lst += right
        return lst