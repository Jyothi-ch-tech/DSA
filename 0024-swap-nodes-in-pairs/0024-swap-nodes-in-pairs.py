# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        
        while curr and curr.next:

            if curr.next is None:
                return head
            
            temp = curr.val
            curr.val = curr.next.val
            curr.next.val = temp

            curr = curr.next.next
            
        return head