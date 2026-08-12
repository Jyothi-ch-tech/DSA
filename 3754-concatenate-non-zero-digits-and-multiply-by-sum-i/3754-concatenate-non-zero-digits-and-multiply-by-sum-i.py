class Solution:
    def sumAndMultiply(self, n: int) -> int:
        temp=0
        sum=0
        while n:
            rem=n%10 
            if rem!=0:
                temp=temp*10+rem
                sum+=rem
            n//=10 
        return int(str(temp)[::-1]) * sum
            
        