# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        res = [-1, -1]
        min_distance = float("inf")
        pre, cur = head, head.next
        cur_idx = 1
        first_critical_idx = prev_critical_idx = 0

        while cur.next:
            if (cur.val < pre.val and cur.val < cur.next.val) or (cur.val > pre.val and cur.val > cur.next.val):
                if prev_critical_idx == 0:
                    first_critical_idx = cur_idx
                else:
                    min_distance = min(min_distance, cur_idx - prev_critical_idx)
                prev_critical_idx = cur_idx
            cur_idx += 1
            pre = cur
            cur = cur.next

        if min_distance != float("inf"):
            max_distance = prev_critical_idx - first_critical_idx
            res = [min_distance, max_distance]

        return res