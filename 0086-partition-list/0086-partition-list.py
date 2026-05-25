# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]: 
        dummy = ListNode(0)
        temp = dummy
        curr = head
        prev = None
        while curr:
            if curr.val < x:
                temp.next = ListNode(curr.val)
                temp = temp.next
            curr = curr.next
        curr = head
        while curr:
            if curr.val >= x:
                temp.next = ListNode(curr.val)
                temp = temp.next
            curr = curr.next
        return dummy.next