class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        arr=s.split()
        return len(arr)==len(pattern) and len(set(arr))==len(set(pattern))==len(set(zip(pattern,arr)))      