class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        res=0
        n,m=len(nums1),len(nums2)
        i,j=0,0
        while i<n and j<m:
            while j<m and nums2[j]>=nums1[i]:
                j+=1
            res=max(res,j-1-i)
            i+=1
        return res
        