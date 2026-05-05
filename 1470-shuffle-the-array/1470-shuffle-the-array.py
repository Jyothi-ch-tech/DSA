class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        nums1=nums[:n]
        nums2=nums[n:]
        temp=[0]*2*n
        j=0
        for i in range(0,2*n-1,2):
            temp[i]=nums1[j]
            temp[i+1]=nums2[j]
            j+=1
        return temp
        


        