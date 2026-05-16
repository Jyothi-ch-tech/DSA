# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        
        for head in lists:
            while head:
                arr.append(head.val)
                head = head.next
        
        arr.sort()
        
        dummy = ListNode(0)
        curr = dummy
        
        for num in arr:
            curr.next = ListNode(num)
            curr = curr.next
        
        return dummy.next
        