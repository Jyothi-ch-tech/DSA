class Solution:
    def numberOfSpecialChars(self, word: str) -> int: 
        count=0
        w=set(word) 
        for i in w:
            if (ord(i)>=ord("A") and ord(i)<=ord("Z")):
                if chr(ord(i)+32) in word:
                    count+=1 
            else:
                if chr(ord(i)-32) in word:
                    count+=1  
        return count//2
        