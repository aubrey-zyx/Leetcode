# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None

        mid = self.find_mid(head)
        root = TreeNode(mid.val)

        # Base case when there is only one element in the linked list
        if head == mid:
            return root

        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)
        return root

    def find_mid(self, head):
        prev = None  # pointer used to disconnect the left half from the mid node
        slow = fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        if prev:
            prev.next = None
        return slow


# Recursion + Conversion to Array
class Solution2:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        vals = []
        cur = head
        while cur:
            vals.append(cur.val)
            cur = cur.next

        def convert(l, r):
            if l > r:
                return None

            mid = (l + r) // 2
            root = TreeNode(vals[mid])

            if l == r:
                return root

            root.left = convert(l, mid - 1)
            root.right = convert(mid + 1, r)
            return root

        return convert(0, len(vals) - 1)


# Inorder
class Solution3:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def convert(l, r):
            nonlocal head

            if l > r:
                return None

            mid = (l + r) // 2
            left = convert(l, mid - 1)
            root = TreeNode(head.val)
            root.left = left
            head = head.next
            root.right = convert(mid + 1, r)
            return root

        return convert(0, self.get_length(head) - 1)

    def get_length(self, head):
        cur = head
        res = 0
        while cur:
            cur = cur.next
            res += 1
        return res