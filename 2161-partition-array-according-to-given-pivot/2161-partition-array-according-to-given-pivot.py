class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n1=[]
        n2=[]
        np=[]
        for num in nums:
            if num<pivot:
                n1.append(num) 
            elif num==pivot:
                np.append(num)
            else:
                n2.append(num)
        return n1+np+n2
            
            
        