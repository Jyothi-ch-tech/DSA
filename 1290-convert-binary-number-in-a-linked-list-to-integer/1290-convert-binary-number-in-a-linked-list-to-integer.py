# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        s=""
        curr=head 
        while curr:
            s+=str(curr.val)
            curr=curr.next 
        ans=0
        j=0
        for i in range(len(s)-1,-1,-1):
            ans+=((2**j)*int(s[i]))
            j+=1
        return ans
            
        