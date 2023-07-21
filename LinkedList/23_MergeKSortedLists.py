# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return

        def divideAndConquer(left, right):
            if left == right:
                return lists[left]
            mid = left + (right - left) // 2
            l1 = divideAndConquer(left, mid)
            l2 = divideAndConquer(mid + 1, right)
            return mergeTwoLists(l1, l2)

        def mergeTwoLists(l1, l2):
            if not (l1 and l2):
                return l1 if l1 else l2
            if l1.val < l2.val:
                l1.next = mergeTwoLists(l1.next, l2)
                return l1
            else:
                l2.next = mergeTwoLists(l2.next, l1)
                return l2

        return divideAndConquer(0, len(lists) - 1)