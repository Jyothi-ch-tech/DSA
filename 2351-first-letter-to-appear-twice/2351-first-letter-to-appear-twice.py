class Solution:
    def repeatedCharacter(self, s: str) -> str:
        f={}
        for ch in s:
            if ch not in f:
                f[ch]=1 
            else:
                f[ch]+=1
                if f[ch]==2:
                    return ch
        