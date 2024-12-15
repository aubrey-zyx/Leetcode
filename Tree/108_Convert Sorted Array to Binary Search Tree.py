# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def preorder(l, r):
            if l > r:
                return None
            p = (l + r) // 2
            root = TreeNode(nums[p])
            root.left = preorder(l, p - 1)
            root.right = preorder(p + 1, r)
            return root

        return preorder(0, len(nums) - 1)