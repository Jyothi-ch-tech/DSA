class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[0]*n
        leftSum=[0]*n 
        leftSum[0]=nums[0] 
        rightSum=[0]*n
        rightSum[-1]=nums[-1] 
        for i in range(1,n):
            leftSum[i]=nums[i]+leftSum[i-1]
        for i in range(n-2,-1,-1):
            rightSum[i]=nums[i]+rightSum[i+1]
        for i in range(n):
            ans[i] = abs(leftSum[i] - rightSum[i])
        return ans
            

        