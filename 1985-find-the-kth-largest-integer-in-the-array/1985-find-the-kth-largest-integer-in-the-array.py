class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        n=len(nums)
        temp=[]
        for num in nums:
            temp.append(int(num))
        temp=sorted(temp)
        return str(temp[n-k])