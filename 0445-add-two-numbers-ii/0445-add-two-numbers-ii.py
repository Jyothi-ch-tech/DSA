# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr=l1
        first=0
        second=0
        while curr:
            first=first*10+curr.val 
            curr=curr.next 
        curr=l2
        while curr:
            second=second*10+curr.val 
            curr=curr.next 
        total=first+second
        if total==0:
            return ListNode(0)
        head=None
        while total>0:
            rem=total%10 
            node=ListNode(rem)
            node.next=head
            head=node
            total//=10     
        return head
        

        