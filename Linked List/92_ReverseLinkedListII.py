# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def reverse_linked_list(head: ListNode):
            pre = None
            cur = head
            while cur:
                tmp = cur.next
                cur.next = pre
                pre = cur
                cur = tmp

        dummy = ListNode(-1, head)
        # precursor: node before left_node
        pre = dummy
        for _ in range(left - 1):
            pre = pre.next
        # keep going and find right_node
        right_node = pre
        for _ in range(right - left + 1):
            right_node = right_node.next
        # cut out the sublist
        left_node = pre.next
        succ = right_node.next  # successor: node after right_node
        pre.next = right_node.next = None
        # reverse
        reverse_linked_list(left_node)
        # put it back
        pre.next = right_node
        left_node.next = succ
        return dummy.next


class Solution2:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        pre = dummy
        for _ in range(left - 1):
            pre = pre.next
        cur = pre.next
        for _ in range(right - left):
            move = cur.next    # node to be moved
            cur.next = move.next
            move.next = pre.next
            pre.next = move
        return dummy.next