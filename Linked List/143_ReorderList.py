# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        mid = self.find_middle(head)
        l1 = head
        l2 = mid.next
        mid.next = None
        l2 = self.reverse_list(l2)
        self.merge_list(l1, l2)

    def find_middle(self, head: ListNode):
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse_list(self, head: ListNode):
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre

    def merge_list(self, l1: ListNode, l2: ListNode):
        while l1 and l2:
            l1_tmp, l2_tmp = l1.next, l2.next
            l1.next = l2
            l1 = l1_tmp
            l2.next = l1
            l2 = l2_tmp


class Solution2:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        vec = list()
        node = head
        while node:
            vec.append(node)
            node = node.next
        i, j = 0, len(vec) - 1
        while i < j:
            vec[i].next = vec[j]
            i += 1
            if i == j:
                break
            vec[j].next = vec[i]
            j -= 1
        vec[i].next = None