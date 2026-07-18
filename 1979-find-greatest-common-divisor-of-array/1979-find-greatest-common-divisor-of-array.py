class Solution:
    def findGCD(self, nums: List[int]) -> int:
        num1=min(nums)
        num2=max(nums)
        while num2:
            num1,num2=num2,num1%num2 
        return num1
        