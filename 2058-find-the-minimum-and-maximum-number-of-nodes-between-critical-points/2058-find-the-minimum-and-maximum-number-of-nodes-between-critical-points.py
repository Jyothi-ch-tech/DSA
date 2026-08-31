# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        first = -1
        prev = -1
        min_d = float('inf')
        a, b, c = head, head.next, head.next.next
        i = 1
        while c:
            if (b.val > a.val and b.val > c.val) or (b.val < a.val and b.val < c.val):
                if first == -1:
                    first = i
                if prev != -1:
                    min_d = min(min_d, i - prev)
                prev = i
            a, b, c = b, c, c.next
            i += 1
        if first == -1 or first == prev:
            return [-1, -1]
        return [min_d, prev - first]