# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        cur = head
        while cur:
            stack.append(cur)
            cur = cur.next

        cur = stack.pop()
        maximum = cur.val
        res = ListNode(maximum)
        while stack:
            cur = stack.pop()
            if cur.val >= maximum:
                new_node = ListNode(cur.val)
                new_node.next = res
                res = new_node
                maximum = cur.val

        return res