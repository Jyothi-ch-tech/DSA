class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int: 
        maxi=0 
        count=0
        for i in nums: 
            if i==0:
                maxi=max(count,maxi)
                count=0
            else:
                count+=1 
        maxi=max(count,maxi) 
        return maxi

        