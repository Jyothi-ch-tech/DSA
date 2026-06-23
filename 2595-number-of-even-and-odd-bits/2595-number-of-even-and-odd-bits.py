class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        counte=0
        counto=0
        i=0 
        while n>0:
            if n&1:
                if i%2==0:
                    counte+=1 
                else:
                    counto+=1 
            n=n>>1 
            i+=1 
        return [counte,counto]
        

        
        