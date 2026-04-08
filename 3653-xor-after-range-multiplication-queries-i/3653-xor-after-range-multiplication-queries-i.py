class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        mod=10**9+7
        for row in queries:
            l=row[0]
            r=row[1]
            k=row[2]
            v=row[3]
            idx=l
            while idx<=r:
                nums[idx]=(nums[idx]*v)%mod 
                idx+=k 
        res=0
        for i in nums:
            res^=i 
        return res

        