# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def preorder(node, cur_sum):
            nonlocal count
            if not node:
                return
            cur_sum += node.val
            count += ht[cur_sum - targetSum]
            ht[cur_sum] += 1
            preorder(node.left, cur_sum)
            preorder(node.right, cur_sum)
            ht[cur_sum] -= 1

        count = 0
        ht = defaultdict(int)
        ht[0] = 1
        preorder(root, 0)
        return count