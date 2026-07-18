class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        odd=0
        even=0
        i=1
        while n>0:
            odd+=i 
            even+=(i+1)
            i+=2 
            n-=1 
        while even:
            odd,even=even,odd%even 
        return odd

        