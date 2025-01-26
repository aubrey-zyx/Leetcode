# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def traverse(node):
            if not node:
                return ""
            rep = "(" + traverse(node.left) + ")" + str(node.val) + "(" + traverse(node.right) + ")"
            cnt[rep] += 1
            if cnt[rep] == 2:
                res.append(node)
            return rep

        cnt = defaultdict(int)
        res = []
        traverse(root)
        return res


class Solution2:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def traverse(node):
            if not node:
                return 0
            triplet = (traverse(node.left), node.val, traverse(node.right))
            if triplet not in triplet_to_id:
                triplet_to_id[triplet] = len(triplet_to_id) + 1
            id = triplet_to_id[triplet]
            cnt[id] += 1
            if cnt[id] == 2:
                res.append(node)
            return id

        triplet_to_id = dict()
        cnt = defaultdict(int)
        res = []
        traverse(root)
        return res