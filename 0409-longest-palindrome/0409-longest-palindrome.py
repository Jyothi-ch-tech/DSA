class Solution:
    def longestPalindrome(self, s: str) -> int:
        n=len(s)
        d=dict()
        for i in s:
            if i not in d:
                d[i]=1 
            else: 
                d[i]+=1 
        co=0
        for i in d:
            if d[i]%2==1:
                co+=1 
        if co>1:
            n=n-co+1  
        return n 
        

        