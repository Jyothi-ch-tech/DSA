class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = {}
        for i in ransomNote:
            d[i] = d.get(i, 0) + 1
        f = {}
        for i in magazine:
            f[i] = f.get(i, 0) + 1
        for i in d:
            if f.get(i, 0) < d[i]:
                return False
        return True
    
    
        