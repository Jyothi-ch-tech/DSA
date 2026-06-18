class Solution:
    def pivotInteger(self, n: int) -> int: 
        temp=[]
        for i in range(1,n+1):
            temp.append(i)
        left_sum=0
        total=sum(temp)
        for i, val in enumerate(temp):
            right_sum=total-left_sum-val 
            if right_sum==left_sum:
                return val 
            left_sum+=val
        return -1

        